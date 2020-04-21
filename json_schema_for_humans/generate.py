import json
import os
import re
import shutil
from typing import Any, Dict, List, Optional, TextIO, Tuple, Type, Union

import click
import htmlmin
import jinja2
import markdown2

TEMPLATE_FILE_NAME = "templates/schema_doc.template.html"
CSS_FILE_NAME = "schema_doc.css"

DEFAULT_PATTERN = r"(\[Default - `([^`]+)`\])"
DEPRECATED_PATTERN = r"\[Deprecated"

TYPE_ARRAY = "array"
TYPE_BOOLEAN = "boolean"
TYPE_CONST = "const"
TYPE_ENUM = "enum"
TYPE_INTEGER = "integer"
TYPE_NUMBER = "number"
TYPE_OBJECT = "object"
TYPE_STRING = "string"

DESCRIPTION = "description"
DEFAULT = "default"
ITEMS = "items"
TYPE = "type"
REF = "$ref"

MULTIPLE_OF = "multipleOf"
MAXIMUM = "maximum"
EXCLUSIVE_MAXIMUM = "exclusiveMaximum"
MINIMUM = "minimum"
EXCLUSIVE_MINIMUM = "exclusiveMinimum"


SHORT_DESCRIPTION_NUMBER_OF_LINES = 8


def is_combining(property_dict: Dict[str, Any]) -> bool:
    """Test if a schema is one of the combining schema keyword"""
    return bool({"anyOf", "allOf", "oneOf", "not"}.intersection(property_dict.keys()))


def is_description_short(description: str) -> bool:
    """Check if a description element is short so that we can decide to make the section expandable.
    The heuristic is counting 1 for each line + 1 for each group of 80 characters a line has
    """
    return sum((len(line) / 80 + 1) for line in description.splitlines()) < SHORT_DESCRIPTION_NUMBER_OF_LINES


def is_deprecated(property_dict: Dict[str, Any]) -> bool:
    """Test. Check if a property is deprecated without looking in description"""
    return False


def is_deprecated_look_in_description(property_dict: Dict[str, Any]) -> bool:
    """Test. Check if a property is deprecated looking in description"""
    if DESCRIPTION not in property_dict:
        return False

    return bool(re.match(DEPRECATED_PATTERN, property_dict[DESCRIPTION]))


def resolve_ref(
    property_dict: Dict[str, Any], full_schema: Dict[str, Any], schema_path: List[str]
) -> Tuple[Dict[str, Any], List[str]]:
    """Filter. Resolve references in the supplied property. Return the property unchanged if no references found.

    See https://json-schema.org/understanding-json-schema/structuring.html#reuse
    """
    if REF not in property_dict:
        return property_dict, schema_path

    # Reference found, resolve the path (format "#/a/b/c" or "file.json#/a/b/c", usually "#/definitions/some name")
    pound_split = property_dict[REF].split("#")
    ref_file_path = [x for x in pound_split[0].split("/") if x != ""]
    ref_anchor_path = [x for x in pound_split[1].split("/") if x != ""] if len(pound_split) > 1 else []
    target = full_schema if ref_anchor_path else {}

    # Resolve file path portion of reference and open schema file
    if ref_file_path:
        target_path = schema_path[:-1]
        for ref_path_segment in ref_file_path:
            if ref_path_segment in (".", ""):
                continue
            elif ref_path_segment == "..":
                target_path.pop()
            else:
                target_path.append(ref_path_segment)
        with open(os.path.sep.join(target_path)) as schema_markdown:
            target = json.load(schema_markdown)
    else:
        target_path = schema_path

    # Resolve anchor portion of reference
    for ref_path_segment in ref_anchor_path:
        if ref_path_segment in target:
            target = target[ref_path_segment]
        else:
            target = property_dict
            break

    return target, target_path


def python_to_json(value: Any) -> Any:
    """Filter. Return the value as it needs to be displayed in JSON

    Used to display a string literals more explicitly for default and const values.
    """
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"

    if isinstance(value, str) and not value.startswith('"'):
        return f'"{value}"'

    return value


def get_type_name(property_dict: Dict[str, Any]) -> str:
    """Filter. Return the type of a property taking into account the type of items for array and enum"""

    def _python_type_to_json_type(python_type: Type[Union[str, int, float, bool, list, dict]]) -> str:
        return {
            str: TYPE_STRING,
            int: TYPE_INTEGER,
            float: TYPE_NUMBER,
            bool: TYPE_BOOLEAN,
            list: TYPE_ARRAY,
            dict: TYPE_OBJECT,
        }.get(python_type, TYPE_STRING)

    def _enum_type(enum_values: List[Any]) -> str:
        enum_type_names = [
            _python_type_to_json_type(python_type_name) for python_type_name in set(type(v) for v in enum_values)
        ]
        if enum_type_names:
            return f"{TYPE_ENUM} (of {' or '.join(enum_type_names)})"

        return TYPE_ENUM

    def _add_subtype_if_array(type_name: str):
        if type_name == TYPE_ARRAY:
            items = property_dict.get(ITEMS, {})
            if not items:
                return type_name

            subtype = items.get(TYPE)
            if TYPE_ENUM in items:
                subtype = _enum_type(items[TYPE_ENUM])

            if not subtype:
                # Too complex to guess items
                return type_name

            type_name = f"{type_name} of {subtype}"

        return type_name

    if TYPE_CONST in property_dict:
        return TYPE_CONST
    if TYPE_ENUM in property_dict:
        return _enum_type(property_dict[TYPE_ENUM])

    type_names: Union[str, List[str]] = property_dict.get(TYPE) or TYPE_OBJECT

    if isinstance(type_names, str):
        type_names = [type_names]

    type_names = [_add_subtype_if_array(type_name) for type_name in type_names]

    return ", ".join(type_names[:-1]) + (" or " if len(type_names) > 1 else "") + type_names[-1]


def get_description(description: Optional[str]) -> str:
    """Filter. Get the description of a property or an empty string"""
    return description or ""


def get_description_remove_default(description: Optional[str]) -> str:
    """Filter. From the description attribute of a property, return the description without any default values in it. Will also convert None to an
    empty string.
    """
    if not description:
        return ""

    match = re.match(DEFAULT_PATTERN, description)
    if not match:
        return description

    return description[match.span(1)[1] :].lstrip()


def get_default(property_dict: Dict[str, Any]) -> Tuple[Optional[Any], bool]:
    """Filter. Return the default value for a property"""
    if DEFAULT in property_dict:
        return property_dict[DEFAULT], True

    return None, False


def get_default_look_in_description(property_dict: Dict[str, Any]) -> Tuple[Optional[Any], bool]:
    """Filter. Get the default value of a JSON Schema property. If not set, look for it in the description.

    Return the found default value if any and whether it has found one
    """
    if DEFAULT in property_dict:
        return property_dict[DEFAULT], True

    description = property_dict.get(DESCRIPTION)
    if not description:
        return None, False

    match = re.match(DEFAULT_PATTERN, description)
    if not match:
        return None, False

    default = match.group(2)
    try:
        default = json.loads(default)
    except json.decoder.JSONDecodeError:
        pass
    return default, True


def get_numeric_restrictions_text(property_dict: Dict[str, Any], before_value: str = "", after_value: str = "") -> str:
    """Filter. Get the text to display about restrictions on a numeric type(integer or number)"""
    multiple_of = property_dict.get(MULTIPLE_OF)
    maximum = property_dict.get(MAXIMUM)
    exclusive_maximum = property_dict.get(EXCLUSIVE_MAXIMUM)
    minimum = property_dict.get(MINIMUM)
    exclusive_minimum = property_dict.get(EXCLUSIVE_MINIMUM)

    # Fix minimum and exclusive_minimum both there
    if minimum is not None and exclusive_minimum is not None:
        if minimum <= exclusive_minimum:
            exclusive_minimum = None
        else:
            minimum = None

    minimum_fragment = ""
    if minimum is not None:
        minimum_fragment += f"greater or equal to {before_value}{minimum}{after_value}"
    if exclusive_minimum is not None:
        minimum_fragment += f"strictly greater than {before_value}{exclusive_minimum}{after_value}"

    # Fix maximum and exclusive_maximum both there
    if maximum is not None and exclusive_maximum is not None:
        if maximum > exclusive_maximum:
            exclusive_maximum = None
        else:
            maximum = None

    maximum_fragment = ""
    if maximum is not None:
        maximum_fragment += f"lesser or equal to {before_value}{maximum}{after_value}"
    if exclusive_maximum is not None:
        maximum_fragment += f"strictly lesser than {before_value}{exclusive_maximum}{after_value}"

    result = "Value must be "
    touched = False
    if minimum_fragment:
        touched = True
        result += minimum_fragment
    if maximum_fragment:
        if touched:
            result += " and "
        touched = True
        result += maximum_fragment
    if multiple_of:
        if touched:
            result += " and "
        result += f"a multiple of {before_value}{multiple_of}{after_value}"

    return result if touched else ""


def generate_from_schema(
    schema: Dict[str, Any],
    schema_path: List[str],
    minify: bool = False,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
) -> str:
    md = markdown2.Markdown(extras=["fenced-code-blocks"])
    env = jinja2.Environment()
    env.filters["markdown"] = lambda text: jinja2.Markup(md.convert(text))
    env.filters["python_to_json"] = python_to_json
    env.filters["get_default"] = get_default_look_in_description if default_from_description else get_default
    env.filters["get_type_name"] = get_type_name
    env.filters["get_description"] = get_description_remove_default if default_from_description else get_description
    env.filters["resolve_ref"] = resolve_ref
    env.filters["get_numeric_restrictions_text"] = get_numeric_restrictions_text
    env.tests["combining"] = is_combining
    env.tests["description_short"] = is_description_short
    env.tests["deprecated"] = is_deprecated_look_in_description if deprecated_from_description else is_deprecated

    template_path = os.path.join(os.path.dirname(__file__), TEMPLATE_FILE_NAME)
    with open(template_path, "r") as template_fp:
        template = env.from_string(template_fp.read())

    rendered = template.render(schema=schema, schema_path=schema_path, expand_buttons=expand_buttons)
    if minify:
        rendered = htmlmin.minify(rendered)

    return rendered


def generate_from_filename(
    schema_file_name: str,
    result_file_name: str,
    minify: bool = True,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
) -> None:
    with open(schema_file_name) as schema_markdown:
        schema = json.load(schema_markdown)
        schema_path = os.path.abspath(schema_file_name).split(os.path.sep)

    rendered_schema_doc = generate_from_schema(
        schema,
        schema_path,
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
    )

    copy_css_to_target(result_file_name)

    with open(result_file_name, "w") as result_schema_doc:
        result_schema_doc.write(rendered_schema_doc)


def generate_from_file_object(
    schema_file: TextIO,
    result_file: TextIO,
    minify: bool,
    deprecated_from_description: bool,
    default_from_description: bool,
    expand_buttons: bool,
) -> None:
    """Generate the JSON schema documentation from opened file objects for both input and output files. The
    result_file should be opened in write mode.
    """
    schema_path = os.path.abspath(schema_file.name).split(os.path.sep)
    result = generate_from_schema(
        json.load(schema_file),
        schema_path,
        minify,
        deprecated_from_description,
        default_from_description,
        expand_buttons,
    )

    copy_css_to_target(result_file.name)

    result_file.write(result)


def copy_css_to_target(result_file_path: str) -> None:
    """Copy the CSS file needed to display the resulting page to the directory containing the result file"""
    target_directory = os.path.dirname(result_file_path)
    css_directory = os.path.dirname(__file__)
    if target_directory != css_directory:
        try:
            shutil.copy(os.path.join(css_directory, CSS_FILE_NAME), os.path.join(target_directory, CSS_FILE_NAME))
        except shutil.SameFileError:
            print(f"Not copying {CSS_FILE_NAME} to {os.path.abspath(target_directory)}, file already exists")


@click.command()
@click.argument("schema_file", nargs=1, type=click.File("r", encoding="utf-8"))
@click.argument("result_file", nargs=1, type=click.File("w+", encoding="utf-8"), default="schema_doc.html")
@click.option("--minify/--no-minify", default=True, help="Run minification om the HTML result")
@click.option(
    "--deprecated-from-description", is_flag=True, help="Look in the description to find if an attribute is deprecated"
)
@click.option(
    "--default-from-description", is_flag=True, help="Look in the description to find an attribute default value"
)
@click.option("--expand-buttons", is_flag=True, help="Add 'Expand all' and 'Collapse all' buttons at the top")
def main(
    schema_file: TextIO,
    result_file: TextIO,
    minify: bool,
    deprecated_from_description: bool,
    default_from_description: bool,
    expand_buttons: bool,
) -> None:
    generate_from_file_object(
        schema_file, result_file, minify, deprecated_from_description, default_from_description, expand_buttons
    )


if __name__ == "__main__":
    main()
