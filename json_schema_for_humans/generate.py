import copy
import json
import os
import re
import shutil
from collections import defaultdict
from typing import Any, Dict, List, Optional, TextIO, Tuple, Type, Union

import click
import htmlmin
import jinja2
import markdown2

TEMPLATE_FILE_NAME = "templates/schema_doc.template.html"
CSS_FILE_NAME = "schema_doc.css"
JS_FILE_NAME = "schema_doc.min.js"

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
EXAMPLES = "examples"
ITEMS = "items"
TYPE = "type"
REF = "$ref"

MULTIPLE_OF = "multipleOf"
MAXIMUM = "maximum"
EXCLUSIVE_MAXIMUM = "exclusiveMaximum"
MINIMUM = "minimum"
EXCLUSIVE_MINIMUM = "exclusiveMinimum"


SHORT_DESCRIPTION_NUMBER_OF_LINES = 8


def defaultdict_list() -> Dict[Any, List]:
    return defaultdict(list)


paths_to_id: Dict[str, Dict[str, str]] = defaultdict(defaultdict)
resolved_references_by_file: Dict[str, Dict[str, List[Tuple[str, str]]]] = defaultdict(defaultdict_list)


def is_combining(property_dict: Dict[str, Any]) -> bool:
    """Test if a schema is one of the combining schema keyword"""
    return bool({"anyOf", "allOf", "oneOf", "not"}.intersection(property_dict.keys()))


def is_text_short(text: str) -> bool:
    """Check if a string is short so that we can decide whether to make the section containing it expandable or not.
    The heuristic is counting 1 for each line + 1 for each group of 80 characters a line has
    """
    return sum((len(line) / 80 + 1) for line in str(text).splitlines()) < SHORT_DESCRIPTION_NUMBER_OF_LINES


def is_deprecated(property_dict: Dict[str, Any]) -> bool:
    """Test. Check if a property is deprecated without looking in description"""
    return False


def is_deprecated_look_in_description(property_dict: Dict[str, Any]) -> bool:
    """Test. Check if a property is deprecated looking in description"""
    if DESCRIPTION not in property_dict:
        return False

    return bool(re.match(DEPRECATED_PATTERN, property_dict[DESCRIPTION]))


def resolve_ref(
    property_dict: Dict[str, Any],
    full_schema: Dict[str, Any],
    schema_path: str,
    current_path: str,
    link_to_reused_ref: bool,
) -> Tuple[Dict[str, Any], str, str, Optional[str]]:
    """Filter. Resolve references in the supplied property.

    See https://json-schema.org/understanding-json-schema/structuring.html#reuse

    :param property_dict: The dict for the current property that can contain a "$ref" key
    :param full_schema: The complete current schema, used for references inside the same file
    :param schema_path: Path to the current schema
    :param current_path: Path to property_dict from full_schema. Used to detect recursive definitions
    :param link_to_reused_ref: If True, will attempt to resolve a reference as being reused.
                               If False, will only resolve references if they are recursive
    :return: The resolved schema at reference (property_dict unchanged if no references found),
             the path to the schema that contained the references,
             the path to the resolved property from the root of the schema,
             and whether the resolved reference is recursive
    """
    current_path = current_path.lstrip("/")

    reference_path = property_dict.get(REF)
    if not reference_path:
        return property_dict, schema_path, current_path, None

    # Reference found, resolve the path (format "#/a/b/c", "file.json#/a/b/c", or "file.json")
    if "#" not in reference_path:
        file_path_part = reference_path
        anchor_part = ""
    else:
        file_path_part, anchor_part = reference_path.split("#", maxsplit=1)
        anchor_part = anchor_part.lstrip("/")

    # Resolve file path portion of reference
    if file_path_part:
        referenced_schema_path = os.path.abspath(os.path.join(os.path.dirname(schema_path), file_path_part))
    else:
        referenced_schema_path = os.path.abspath(schema_path)

    if anchor_part:
        if link_to_reused_ref:
            # Check if the referenced part was already documented elsewhere
            resolved_schema, resolved_html_id, is_recursive = get_path_id(referenced_schema_path, anchor_part)
            if is_recursive:
                return property_dict, resolved_schema, current_path, resolved_html_id

            # Record that this reference was documented here
            global resolved_references
            resolved_references_by_file[resolved_schema][anchor_part].append(
                (os.path.abspath(schema_path), current_path)
            )

        # TODO: current_path does not carry the filename, should it?
        # Check for definition referencing a parent element
        split_anchor_part = anchor_part.split("/")
        split_current_path = current_path.split("/")
        is_parent = True
        for i, anchor_part_segment in enumerate(split_anchor_part):
            if len(split_current_path) <= i:
                break
            if anchor_part_segment != split_current_path[i]:
                is_parent = False
                break

        if is_parent:
            return property_dict, schema_path, anchor_part, get_path_id(referenced_schema_path, anchor_part)[1]

    # Open schema file
    if file_path_part:
        with open(referenced_schema_path) as schema_markdown:
            target = json.load(schema_markdown)
    else:
        target = full_schema if anchor_part else {}

    if anchor_part:
        # Resolve anchor portion of reference
        for ref_path_segment in anchor_part.split("/"):
            if not ref_path_segment:
                continue

            if ref_path_segment in target:
                target = target[ref_path_segment]
            else:
                target = property_dict
                break

    # Apply other attributes (description, title, etc.) from the referencing schema to the referenced schema
    # The JSON schema specification does not say if we should do that or not, but I think it is useful
    result_schema = copy.deepcopy(target)
    for k, v in property_dict.items():
        if k == REF:
            continue
        result_schema[k] = v

    return result_schema, referenced_schema_path, anchor_part, None


def record_path_id(path: str, schema_path: str, html_id: str) -> None:
    """Filter. Record the link between a path to an element in the schema and the HTML id added to the documentation
    element for it

    Used for recursive definitions, where an anchor link is needed

    :param path: path to an element in the schema. The format is a list of dictionary keys and array index joined by '/'
    :param schema_path: File path to the current schema
    :param html_id: Unique HTML id of the element that documents the schema at this path
    """
    global paths_to_id
    paths_to_id[os.path.abspath(schema_path)][path] = html_id


def get_path_id(schema_path: str, path: str) -> Tuple[str, str, bool]:
    """Get the HTML id for a schema path.

    Uses links recorded using the filter "record_path_id"

    :param schema_path: Path to the current schema on the file system
    :param path: path to an element in the schema. The format is a list of dictionary keys and array index joined by '/'
    :return: The HTML id to the documentation section for the provided schema path, if found.
             The path itself if not found
    """
    paths_to_id_for_this_schema = paths_to_id[schema_path]

    if path in paths_to_id_for_this_schema:
        return schema_path, paths_to_id_for_this_schema[path], True

    for referenced_schema, referenced_path in resolved_references_by_file[schema_path][path]:
        if referenced_path in paths_to_id[referenced_schema]:
            return referenced_schema, paths_to_id[referenced_schema][referenced_path], True

    return schema_path, path, False


def get_undocumented_required_properties(property_dict: Dict[str, Any]) -> List[str]:
    required_properties = property_dict.get("required", [])
    documented_properties = property_dict.get("properties", {}).keys()

    undocumented = []
    for property_name in required_properties:
        if property_name not in documented_properties:
            undocumented.append(property_name)

    return undocumented


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


def to_pretty_json(value: Any) -> str:
    """Filter. Return a pretty printed JSON representation of an object

    Used instead of the built-in tojson filter to be able to display special characters (ensure_ascii parameter)
    """
    try:
        return json.dumps(value, indent=4, separators=(",", ": "), ensure_ascii=False)
    except:
        return str(value)


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


def escape_property_name_for_id(property_name: str) -> str:
    """Filter. Escape unsafe characters in a property name so that it can be used in a HTML id"""

    escaped = re.sub("[^0-9a-zA-Z_,.-]", "_", str(property_name))
    if not escaped[0].isalpha():
        escaped = "a" + escaped
    return escaped


def generate_id_for_pattern_property(parent_property_name: str, current_index: int):
    """Filter. Generate a unique identifier for a pattern property that can be used in a HTML id"""
    id_string = parent_property_name + "_" + str(current_index)
    if not id_string[0].isalpha():
        id_string = "a" + id_string
    return id_string


def generate_from_schema(
    schema: Dict[str, Any],
    schema_path: str,
    minify: bool = False,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    link_to_reused_ref: bool = True,
) -> str:
    global resolved_references
    resolved_references = defaultdict(defaultdict_list)
    global paths_to_id
    paths_to_id = defaultdict(defaultdict)

    md = markdown2.Markdown(extras=["fenced-code-blocks"])
    env = jinja2.Environment()
    env.filters["markdown"] = lambda text: jinja2.Markup(md.convert(text))
    env.filters["python_to_json"] = python_to_json
    env.filters["get_default"] = get_default_look_in_description if default_from_description else get_default
    env.filters["get_type_name"] = get_type_name
    env.filters["get_description"] = get_description_remove_default if default_from_description else get_description
    env.filters["resolve_ref"] = resolve_ref
    env.filters["get_numeric_restrictions_text"] = get_numeric_restrictions_text
    env.filters["escape_property_name_for_id"] = escape_property_name_for_id
    env.filters["generate_id_for_pattern_property"] = generate_id_for_pattern_property
    env.filters["to_pretty_json"] = to_pretty_json
    env.filters["record_path_id"] = record_path_id
    env.filters["get_undocumented_required_properties"] = get_undocumented_required_properties
    env.tests["combining"] = is_combining
    env.tests["description_short"] = is_text_short
    env.tests["deprecated"] = is_deprecated_look_in_description if deprecated_from_description else is_deprecated

    template_path = os.path.join(os.path.dirname(__file__), TEMPLATE_FILE_NAME)
    with open(template_path, "r") as template_fp:
        template = env.from_string(template_fp.read())

    if isinstance(schema_path, list):
        # Backward compatibility
        schema_path = os.path.sep.join(schema_path)
    schema_path = os.path.abspath(schema_path)

    rendered = template.render(
        schema=schema, schema_path=schema_path, expand_buttons=expand_buttons, link_to_reused_ref=link_to_reused_ref
    )

    if minify:
        rendered = htmlmin.minify(rendered)

    return rendered


def generate_from_filename(
    schema_file_name: str,
    result_file_name: str,
    minify: bool = True,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    copy_css: bool = True,
    copy_js: bool = True,
    link_to_reused_ref: bool = True,
) -> None:
    with open(schema_file_name, encoding="utf-8") as schema_markdown:
        schema = json.load(schema_markdown)

    rendered_schema_doc = generate_from_schema(
        schema,
        os.path.abspath(schema_file_name),
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        link_to_reused_ref=link_to_reused_ref,
    )

    copy_css_and_js_to_target(result_file_name, copy_css, copy_js)

    with open(result_file_name, "w", encoding="utf-8") as result_schema_doc:
        result_schema_doc.write(rendered_schema_doc)


def generate_from_file_object(
    schema_file: TextIO,
    result_file: TextIO,
    minify: bool,
    deprecated_from_description: bool,
    default_from_description: bool,
    expand_buttons: bool,
    copy_css: bool = True,
    copy_js: bool = True,
    link_to_reused_ref: bool = True,
) -> None:
    """Generate the JSON schema documentation from opened file objects for both input and output files. The
    result_file should be opened in write mode.
    """
    result = generate_from_schema(
        json.load(schema_file),
        os.path.abspath(schema_file.name),
        minify,
        deprecated_from_description,
        default_from_description,
        expand_buttons,
        link_to_reused_ref,
    )

    copy_css_and_js_to_target(result_file.name, copy_css, copy_js)

    result_file.write(result)


def copy_css_and_js_to_target(result_file_path: str, copy_css: bool, copy_js: bool) -> None:
    """Copy the CSS and JS files needed to display the resulting page to the directory containing the result file"""
    files_to_copy = []
    if copy_css:
        files_to_copy.append(CSS_FILE_NAME)
    if copy_js:
        files_to_copy.append(JS_FILE_NAME)
    if not files_to_copy:
        return

    target_directory = os.path.dirname(result_file_path)
    source_directory = os.path.dirname(__file__)
    if target_directory == source_directory:
        return

    for file_to_copy in files_to_copy:
        try:
            shutil.copy(os.path.join(source_directory, file_to_copy), os.path.join(target_directory, file_to_copy))
        except shutil.SameFileError:
            print(f"Not copying {file_to_copy} to {os.path.abspath(target_directory)}, file already exists")


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
@click.option("--copy-css/--no-copy-css", default=True, help=f"Copy {CSS_FILE_NAME} to the folder of the result_file")
@click.option("--copy-js/--no-copy-js", default=True, help=f"Copy {JS_FILE_NAME} to the folder of the result_file")
@click.option(
    "--link-to-reused-ref/--no-link-to-reused-ref",
    default=True,
    help="If set and 2 parts of the schema refer to the same definition, the definition will only be rendered once "
    "and all other references will be replaced by a link.",
)
def main(
    schema_file: TextIO,
    result_file: TextIO,
    minify: bool,
    deprecated_from_description: bool,
    default_from_description: bool,
    expand_buttons: bool,
    copy_css: bool,
    copy_js: bool,
    link_to_reused_ref: bool,
) -> None:
    generate_from_file_object(
        schema_file,
        result_file,
        minify,
        deprecated_from_description,
        default_from_description,
        expand_buttons,
        copy_css,
        copy_js,
        link_to_reused_ref,
    )


if __name__ == "__main__":
    main()
