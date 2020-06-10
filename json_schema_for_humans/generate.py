import copy
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, TextIO, Tuple, Type, Union

import click
import htmlmin
import jinja2
import markdown2
from jinja2 import FileSystemLoader
import yaml
from pytz import reference


TEMPLATE_FOLDER = "templates"
TEMPLATE_FILE_NAME = "base.html"
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


class SchemaNode:
    """
    Represents a part of a JSON schema with additional metadata to help with documentation
    """

    def __init__(
        self,
        depth: int,
        file: str,
        path_to_element: List[Union[str, int]],
        html_id: str,
        literal: Union[str, int] = None,
        keywords: Dict[str, "SchemaNode"] = None,
        array_items: List["SchemaNode"] = None,
        refers_to: "SchemaNode" = None,
        is_displayed: bool = True,
    ):
        """

        :param depth: Number of levels from the root of the schema to this node.
        :param file: Real path to the schema file
        :param path_to_element: Path from the root of the schema to the current element
        :param html_id: HTML ID for the current element. Used for anchor links.
        :param literal: If the schema is neither a dict nor an array, it will be kept here
                        Useful for things like description, types, const, enum, etc.
        :param keywords: If the schema is a dict, this will be filled. Otherwise, this stays empty
        :param array_items: If the schema is an array, this will be filled. Otherwise, this stays empty
        :param refers_to: If there is a $ref, this should contain the SchemaNode object for it
        :param is_displayed: Instructs the templates if this part should be fully documented.
                             If false, the description and a link to the referenced element will be generated instead.
                             If false, refers_to needs to be set
        """
        self.depth = depth
        self.file = file
        self.path_to_element = path_to_element
        self.literal = literal
        self.keywords = keywords or {}
        self.array_items = array_items or []
        self.refers_to = refers_to
        self.is_displayed = is_displayed
        self.html_id = html_id or "_".join(path_to_element) or "root"

    @property
    def is_definition(self) -> bool:
        return self.path_to_element and self.path_to_element[0] != "definitions"

    def __eq__(self, other: object) -> bool:
        """For two schema nodes to be considered equals they must represent the same element in the same file"""
        if other is None:
            return False

        if not isinstance(other, SchemaNode):
            return NotImplemented

        return self.file == other.file and self.path_to_element == other.path_to_element


def build_intermediate_representation(
    schema_path: Union[str, TextIO], loaded_schemas: Optional[Dict[str, Any]] = None
) -> SchemaNode:
    """Build a SchemaNode object representing a JSON schema with added metadata to help rendering as a documentation.

    The representation will resolve references and generate HTML ids for elements
    """
    resolved_references: Dict[str, Dict[str, SchemaNode]] = defaultdict(dict)

    def defaultdict_list() -> Dict[Any, List]:
        return defaultdict(list)

    reference_users: Dict[str, Dict[str, List[SchemaNode]]] = defaultdict(defaultdict_list)
    _loaded_schemas: Dict[str, Any]
    if loaded_schemas is None:
        _loaded_schemas = {}
    else:
        assert isinstance(loaded_schemas, dict) and all(
            isinstance(k, str) for k in loaded_schemas.keys()
        ), "loaded_schemas must be Dict[str, Any]"
        _loaded_schemas = loaded_schemas

    # Make sure schema_path is absolute, all symlinks are resolved
    if isinstance(schema_path, Path):
        schema_path = str(schema_path.resolve())
    elif isinstance(schema_path, str):
        schema_path = os.path.realpath(schema_path)
    else:
        # Assuming schema_path is a file object (TextIO)
        schema_path = os.path.realpath(schema_path.name)

    def _record_ref(schema_real_path: str, path_to_element: List[Union[str, int]], current_node: SchemaNode) -> None:
        """Record that the node is describing the schema at the provided path"""
        resolved_references[schema_real_path]["/".join(str(e) for e in path_to_element)] = current_node

    def _resolve_ref(current_node: SchemaNode, schema: Union[Dict, List, int, str]) -> Optional[SchemaNode]:
        """Resolve the $ref keyword

        If there is no $ref, return None.
        If there is a referenced element that was never encountered before, build that element and return it.
        If there is a referenced element that was already encountered, return it.

        This method also makes sure that the final element to be fully documented is the one that is the less nested
        so that the information is closer to the user.
        """
        if not isinstance(schema, Dict) or REF not in schema:
            return None

        reference_path = schema.get(REF)
        if not reference_path:
            return None

        # Reference found, resolve the path (format "#/a/b/c", "file.json#/a/b/c", or "file.json")
        if "#" not in reference_path:
            file_path_part = reference_path
            anchor_part = ""
        else:
            file_path_part, anchor_part = reference_path.split("#", maxsplit=1)
            anchor_part = anchor_part.strip("/")

        # Resolve file path portion of reference
        if file_path_part:
            referenced_schema_path = os.path.realpath(os.path.join(os.path.dirname(current_node.file), file_path_part))
        else:
            referenced_schema_path = os.path.realpath(current_node.file)

        def _find_reference(path: str, anchor_path: str) -> Optional[SchemaNode]:
            resolved_references_for_this_schema = resolved_references[path]
            return resolved_references_for_this_schema.get(anchor_path)

        # Check if already loaded
        found_reference = _find_reference(referenced_schema_path, anchor_part)

        if found_reference == current_node:
            found_reference = None

        if found_reference:
            while not found_reference.is_displayed and found_reference.refers_to:
                if found_reference.refers_to == current_node:
                    break
                found_reference = found_reference.refers_to

            # Is someone else using the reference?
            reference_users_for_this_schema = reference_users[found_reference.file][anchor_part]
            reference_users[referenced_schema_path][anchor_part].append(current_node)
            if reference_users_for_this_schema:
                other_user = None
                other_is_better = False
                i_am_better = False
                for user in reference_users_for_this_schema:
                    if user == current_node or not user.is_displayed:
                        continue

                    if not other_user:
                        other_user = user

                    if user.depth < other_user.depth:
                        other_user = user

                    if other_user.depth < current_node.depth:
                        other_user = user
                        other_is_better = True
                        i_am_better = False
                    elif other_user.depth > current_node.depth:
                        other_is_better = False
                        i_am_better = True

                # There is at least on other node having the same reference as the current node.
                if other_is_better:
                    # The other referencing node is nearer to the user, so it will now be displayed
                    # We mark the current node as being hidden and linking to the other one
                    other_user.is_displayed = True
                    current_node.is_displayed = False
                    return other_user
                elif i_am_better:
                    # The other referencing node is more nested, it should be hidden and link to the current node
                    # The current node will documented the element referenced by both
                    other_user.is_displayed = False
                    other_user.refers_to = current_node
                    current_node.is_displayed = True
                    return found_reference
                else:
                    # Both nodes are the same depth. The other having been seen first,
                    # this node will be hidden and link to it
                    current_node.is_displayed = False
                    return other_user

            return found_reference
        else:
            reference_users[referenced_schema_path][anchor_part].append(current_node)

        # Not an existing reference, so it shall be built
        referenced_schema_path_to_element = anchor_part.split("/")
        return _build_node(
            current_node.depth,
            current_node.html_id,
            referenced_schema_path,
            referenced_schema_path_to_element,
            _load_schema(referenced_schema_path, referenced_schema_path_to_element),
        )

    def _load_schema(schema_file_path: str, path_to_element: List[Union[str, int]]) -> Union[Dict, List, int, str]:
        """Load the schema at the provided path. The path must be a "realpath", meaning absolute and with symlinks
        resolved.

        Loaded paths are kept in memory as to ensure never loading the same file twice
        """
        if schema_file_path in _loaded_schemas:
            loaded_schema = _loaded_schemas[schema_file_path]
        else:
            with open(schema_file_path, encoding="utf-8") as schema_fp:
                loaded_schema = yaml.safe_load(schema_fp)
            _loaded_schemas[schema_file_path] = loaded_schema

        if path_to_element:
            for path_part in path_to_element:
                if not path_part:
                    # Empty string
                    continue
                if isinstance(path_part, str):
                    loaded_schema = loaded_schema[path_part]
                elif isinstance(path_part, int):
                    loaded_schema = loaded_schema[path_part]

        return loaded_schema

    def _build_node(
        depth: int,
        html_id: str,
        schema_file_path: str,
        path_to_element: List[Union[str, int]],
        schema: Union[Dict, List, int, str],
    ) -> SchemaNode:
        """Recursively build a schema representation

        :param depth: Number of levels from the root of the schema to this node. Used when there are references to
                      figure out the less nested one in order to display it.
        :param html_id: HTML ID for the current element. Used for anchor links.
        :param schema_file_path: Real path to the schema (absolute path with symlinks resolved)
        :param path_to_element: Path from the root of the schema to the current element
        :param schema: The JSON schema part being represented
        :return: A representation of the schema
        """
        schema_file_path = os.path.realpath(schema_file_path)

        new_node = SchemaNode(depth, file=schema_file_path, path_to_element=path_to_element, html_id=html_id)
        if html_id == "root":
            html_id = ""

        _record_ref(schema_file_path, path_to_element, new_node)

        if isinstance(schema, dict):
            keywords = {}
            for schema_key, schema_value in schema.items():
                # These won't be needed to render the documentation.
                # The definitions will be reached from references, otherwise they are useless
                if schema_key in ["$id", "$ref", "$schema", "definitions"]:
                    continue

                # Examples are rendered in JSON because they will be represented that way in the documentation,
                # no need for a SchemaNode object
                if schema_key == "examples":
                    keywords[schema_key] = [
                        json.dumps(example, indent=4, separators=(",", ": "), ensure_ascii=False)
                        for example in schema_value
                    ]
                    continue

                # The default value will be printed as-is, no need for a SchemaNode object
                if schema_key == "default":
                    keywords[schema_key] = json.dumps(schema_value, ensure_ascii=False)
                    continue

                # Add the property name (correctly escaped) to the ID
                new_html_id = html_id
                new_depth = depth
                if schema_key != "properties":
                    new_depth += 1
                    new_html_id = new_html_id + ("_" if html_id else "") + escape_property_name_for_id(schema_key)

                property_path = copy.deepcopy(path_to_element) + [schema_key]
                keywords[schema_key] = _build_node(
                    new_depth, new_html_id, schema_file_path, property_path, schema_value
                )
            new_node.keywords = keywords
        elif isinstance(schema, list):
            array_items = []
            for i, element in enumerate(schema):
                # Add the property name (correctly escaped) to the ID
                new_html_id = html_id + ("_" if html_id else "") + "i" + str(i)

                array_items.append(
                    _build_node(depth + 1, new_html_id, schema_file_path, path_to_element + [i], element)
                )
            new_node.array_items = array_items

        else:
            new_node.literal = schema

        new_node.refers_to = _resolve_ref(new_node, schema)

        return new_node

    intermediate_representation = _build_node(0, "", schema_path, [], _load_schema(schema_path, []))

    return intermediate_representation


def is_combining(schema_node: SchemaNode) -> bool:
    """Test if a schema is one of the combining schema keyword"""
    return bool({"anyOf", "allOf", "oneOf", "not"}.intersection(schema_node.keywords.keys()))


def is_text_short(text: str) -> bool:
    """Check if a string is short so that we can decide whether to make the section containing it expandable or not.
    The heuristic is counting 1 for each line + 1 for each group of 80 characters a line has
    """
    return sum((len(line) / 80 + 1) for line in str(text).splitlines()) < SHORT_DESCRIPTION_NUMBER_OF_LINES


def is_deprecated(property_dict: Dict[str, Any]) -> bool:
    """Test. Check if a property is deprecated without looking in description"""
    return False


def is_deprecated_look_in_description(schema_node: SchemaNode) -> bool:
    """Test. Check if a property is deprecated looking in description"""
    if DESCRIPTION not in schema_node.keywords:
        return False

    return bool(re.match(DEPRECATED_PATTERN, schema_node.keywords[DESCRIPTION].literal))


def get_required_properties(schema_node: SchemaNode) -> List[str]:
    required_properties = schema_node.keywords.get("required") or []
    if required_properties:
        required_properties = [p.literal for p in required_properties.array_items]

    return required_properties


def get_undocumented_required_properties(schema_node: SchemaNode) -> List[str]:
    required_properties = get_required_properties(schema_node)

    documented_properties = schema_node.keywords.get("properties")
    documented_properties = documented_properties.keywords.keys() if documented_properties else []

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


def get_type_name(schema_node: SchemaNode) -> str:
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

    def _enum_type(enum_values: List[SchemaNode]) -> str:
        enum_type_names = [
            _python_type_to_json_type(python_type_name)
            for python_type_name in set(type(v.literal) for v in enum_values)
        ]
        if enum_type_names:
            return f"{TYPE_ENUM} (of {' or '.join(enum_type_names)})"

        return TYPE_ENUM

    def _add_subtype_if_array(type_name: str):
        if type_name == TYPE_ARRAY:
            items = schema_node.keywords.get(ITEMS, None)
            if not items:
                return type_name

            subtype = items.keywords.get(TYPE)
            if subtype:
                subtype = subtype.literal
            if TYPE_ENUM in items.keywords:
                subtype = _enum_type(items.keywords[TYPE_ENUM].array_items)

            if not subtype:
                # Too complex to guess items
                return type_name

            type_name = f"{type_name} of {subtype}"

        return type_name

    if TYPE_CONST in schema_node.keywords:
        return TYPE_CONST
    if TYPE_ENUM in schema_node.keywords:
        return _enum_type(schema_node.keywords[TYPE_ENUM].array_items)

    type_node = schema_node.keywords.get(TYPE)
    if type_node:
        if type_node.array_items:
            type_names = [node.literal for node in type_node.array_items]
        else:
            type_names = [type_node.literal]
    else:
        type_names = [TYPE_OBJECT]

    type_names = [_add_subtype_if_array(type_name) for type_name in type_names]

    return ", ".join(type_names[:-1]) + (" or " if len(type_names) > 1 else "") + type_names[-1]


def _get_description(schema_node: SchemaNode) -> str:
    description = ""
    description_node = schema_node.keywords.get(DESCRIPTION)
    if description_node:
        description = description_node.literal

    seen = set()
    current_node = schema_node
    while not description and current_node.refers_to:
        if current_node.html_id in seen:
            break
        seen.add(current_node.html_id)
        referenced_schema = current_node.refers_to
        referenced_description_node = referenced_schema.keywords.get(DESCRIPTION)
        if referenced_description_node:
            description = referenced_description_node.literal
        current_node = referenced_schema

    return description


def get_description(schema_node: SchemaNode) -> str:
    """Filter. Get the description of a property or an empty string"""
    return _get_description(schema_node)


def get_description_remove_default(schema_node: SchemaNode) -> str:
    """Filter. From the description attribute of a property, return the description without any default values in it.
    Will also convert None to an empty string.
    """
    description = _get_description(schema_node)
    if not description:
        return ""

    match = re.match(DEFAULT_PATTERN, description)
    if not match:
        return description

    return description[match.span(1)[1] :].lstrip()


def get_default(schema_node: SchemaNode) -> str:
    """Filter. Return the default value for a property"""
    return schema_node.keywords.get(DEFAULT) or ""


def get_default_look_in_description(schema_node: SchemaNode) -> str:
    """Filter. Get the default value of a JSON Schema property. If not set, look for it in the description."""
    default_value = get_default(schema_node)
    if default_value:
        return default_value

    description = schema_node.keywords.get(DESCRIPTION).literal
    if not description:
        return ""

    match = re.match(DEFAULT_PATTERN, description)
    if not match:
        return ""

    return match.group(2)


def get_numeric_restrictions_text(schema_node: SchemaNode, before_value: str = "", after_value: str = "") -> str:
    """Filter. Get the text to display about restrictions on a numeric type(integer or number)"""
    multiple_of = schema_node.keywords.get(MULTIPLE_OF)
    if multiple_of:
        multiple_of = multiple_of.literal
    maximum = schema_node.keywords.get(MAXIMUM)
    if maximum:
        maximum = maximum.literal
    exclusive_maximum = schema_node.keywords.get(EXCLUSIVE_MAXIMUM)
    if exclusive_maximum:
        exclusive_maximum = exclusive_maximum.literal
    minimum = schema_node.keywords.get(MINIMUM)
    if minimum:
        minimum = minimum.literal
    exclusive_minimum = schema_node.keywords.get(EXCLUSIVE_MINIMUM)
    if exclusive_minimum:
        exclusive_minimum = exclusive_minimum.literal

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


def get_local_time() -> str:
    return datetime.now(tz=reference.LocalTimezone()).strftime("%Y-%m-%d at %H:%M:%S %z")


def generate_from_schema(
    schema_file: Union[str, Path, TextIO],
    loaded_schemas: Optional[Dict[str, Any]] = None,
    minify: bool = False,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    link_to_reused_ref: bool = True,
) -> str:

    template_folder = os.path.join(os.path.dirname(__file__), TEMPLATE_FOLDER)
    base_template_path = os.path.join(template_folder, TEMPLATE_FILE_NAME)

    md = markdown2.Markdown(extras=["fenced-code-blocks"])
    loader = FileSystemLoader(template_folder)
    env = jinja2.Environment(loader=loader)
    env.filters["markdown"] = lambda text: jinja2.Markup(md.convert(text))
    env.filters["python_to_json"] = python_to_json
    env.filters["get_default"] = get_default_look_in_description if default_from_description else get_default
    env.filters["get_type_name"] = get_type_name
    env.filters["get_description"] = get_description_remove_default if default_from_description else get_description
    env.filters["get_numeric_restrictions_text"] = get_numeric_restrictions_text
    env.filters["get_required_properties"] = get_required_properties
    env.filters["get_undocumented_required_properties"] = get_undocumented_required_properties
    env.tests["combining"] = is_combining
    env.tests["description_short"] = is_text_short
    env.tests["deprecated"] = is_deprecated_look_in_description if deprecated_from_description else is_deprecated
    env.globals["get_local_time"] = get_local_time

    with open(base_template_path, "r") as template_fp:
        template = env.from_string(template_fp.read())

    if isinstance(schema_file, list):
        # Backward compatibility
        schema_file = os.path.sep.join(schema_file)

    intermediate_schema = build_intermediate_representation(schema_file, loaded_schemas)

    rendered = template.render(
        schema=intermediate_schema, expand_buttons=expand_buttons, link_to_reused_ref=link_to_reused_ref
    )

    if minify:
        rendered = htmlmin.minify(rendered)

    return rendered


def generate_from_filename(
    schema_file_name: Union[str, Path],
    result_file_name: str,
    minify: bool = True,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    copy_css: bool = True,
    copy_js: bool = True,
    link_to_reused_ref: bool = True,
) -> None:
    if isinstance(schema_file_name, str):
        schema_file_name = os.path.realpath(schema_file_name)
    elif isinstance(schema_file_name, Path):
        schema_file_name = str(schema_file_name.resolve())

    rendered_schema_doc = generate_from_schema(
        schema_file_name,
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
        schema_file,
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        link_to_reused_ref=link_to_reused_ref,
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
