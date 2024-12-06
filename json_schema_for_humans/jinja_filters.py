import json
import re
from datetime import datetime
from typing import Any, List, Optional, cast

import yaml
from jinja2 import Environment, pass_environment
from markdown2 import Markdown  # type: ignore
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import YamlLexer
from pygments.lexers.javascript import JavascriptLexer
from pytz import reference

from json_schema_for_humans import const
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from json_schema_for_humans.schema.schema_node import SchemaNode
from json_schema_for_humans.templating_utils import schema_keyword_convert_to_str, schema_keyword_to_str

SHORT_DESCRIPTION_NUMBER_OF_LINES = 8
DEFAULT_PATTERN = r"(\[Default - `([^`]+)`\])"
DEPRECATED_MARKER = r"[Deprecated"


def is_combining(schema_node: SchemaNode) -> bool:
    """Test if a schema is one of the combining schema keyword"""
    return bool({"anyOf", "allOf", "oneOf", "not"}.intersection(schema_node.keywords.keys()))


def is_text_short(text: str) -> bool:
    """Check if a string is short so that we can decide whether to make the section containing it expandable or not.
    The heuristic is counting 1 for each line + 1 for each group of 80 characters a line has
    """
    return (
        sum((len(line) / const.LINE_WIDTH + 1) for line in str(text).splitlines()) < SHORT_DESCRIPTION_NUMBER_OF_LINES
    )


def is_deprecated(_schema: SchemaNode) -> bool:
    """Test. Check if a property is deprecated without looking in description"""
    return False


def is_deprecated_look_in_description(schema_node: SchemaNode) -> bool:
    """Test. Check if a property is deprecated looking in description"""
    if const.DESCRIPTION not in schema_node.keywords:
        return False

    return bool(DEPRECATED_MARKER in (schema_node.keywords[const.DESCRIPTION].literal_str or ""))


def get_required_properties(schema_node: SchemaNode) -> List[str]:
    required_properties_node: Optional[SchemaNode] = schema_node.keywords.get("required")
    required_properties: List[str] = []
    if required_properties_node:
        required_properties = [p.literal_str for p in required_properties_node.array_items if p.literal_str]

    return required_properties


def get_first_property(schema_node: SchemaNode) -> Any:
    """
    Filter. get first property of given schema no matter the property key
    Usage:
    md template does not recurse on schema to render the if portion
    instead it renders the if in the heading directly
    """
    properties = schema_node.properties
    if not properties:
        return None
    first_property_name = next(iter(properties))
    return properties[first_property_name]


def get_undocumented_required_properties(schema_node: SchemaNode) -> List[str]:
    """Get the name of the properties that are required but not documented with their own node"""
    return [prop for prop in get_required_properties(schema_node) if prop not in schema_node.properties.keys()]


def python_to_json(value: Any) -> Any:
    """Filter. Return the value as it needs to be displayed in JSON

    Used to display a string literals more explicitly for default and const values.
    """
    if value is None:
        return "null"

    return json.dumps(value, indent=4, separators=(",", ": "), ensure_ascii=False)


@pass_environment
def get_description(env: Environment, schema_node: SchemaNode) -> str:
    """Filter. Get the description of a property or an empty string"""
    description = schema_node.description
    return get_description_literal(env, description)


@pass_environment
def get_description_literal(env: Environment, description: str) -> str:
    """Filter. Get the description of a property or an empty string"""

    config: GenerationConfiguration = cast(GenerationConfiguration, env.globals["jsfh_config"])
    if config.default_from_description:
        match = re.match(DEFAULT_PATTERN, description)
        if match:
            description = description[match.span(1)[1] :].lstrip()

    if description and not config.result_extension == "md" and config.description_is_markdown:
        # Markdown templates are expected to already have Markdown descriptions
        md: Markdown = env.globals["jsfh_md"]
        description = md.convert(description)

    return description


def get_default(schema_node: SchemaNode) -> str:
    """Filter. Return the default value for a property"""
    return str(schema_node.default_value) if schema_node.default_value is not None else ""


def get_default_look_in_description(schema_node: SchemaNode) -> str:
    """Filter. Get the default value of a JSON Schema property. If not set, look for it in the description."""
    default_value = schema_node.default_value
    if default_value:
        return default_value

    description = schema_keyword_to_str(schema_node, const.DESCRIPTION)
    if not description:
        return ""

    match = re.match(DEFAULT_PATTERN, description)
    if not match:
        return ""

    return match.group(2)


def get_numeric_restrictions_text(schema_node: SchemaNode, before_value: str = "", after_value: str = "") -> str:
    """Filter. Get the text to display about restrictions on a numeric type(integer or number)"""
    multiple_of = schema_keyword_convert_to_str(schema_node, const.MULTIPLE_OF)
    maximum = schema_keyword_convert_to_str(schema_node, const.MAXIMUM)
    exclusive_maximum = schema_keyword_convert_to_str(schema_node, const.EXCLUSIVE_MAXIMUM)
    minimum = schema_keyword_convert_to_str(schema_node, const.MINIMUM)
    exclusive_minimum = schema_keyword_convert_to_str(schema_node, const.EXCLUSIVE_MINIMUM)

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


def deprecated(config, schema: SchemaNode) -> bool:
    return is_deprecated_look_in_description(schema) if config.deprecated_from_description else is_deprecated(schema)


def first_line(example_text: str) -> str:
    """Filter. Retrieve first line of string + add ... at the end if text has multiple lines cut line at max_length"""
    lines = example_text.splitlines()
    result = lines[0]
    etc = len(lines) > 1
    return f"{result}{' ...' if etc else ''}"


def get_local_time() -> str:
    return datetime.now(tz=reference.LocalTimezone()).strftime("%Y-%m-%d at %H:%M:%S %z")


def highlight_json_example(example_text: str) -> str:
    """Filter. Return an highlighted version of the provided JSON text"""
    return highlight(example_text, JavascriptLexer(), HtmlFormatter())


def yaml_example(example_text: str) -> str:
    """Filter. Return a YAML version of the provided JSON text"""
    loaded_example = json.loads(example_text)
    if not isinstance(loaded_example, dict):
        # YAML dump does not like things that are not object
        return str(loaded_example)
    return yaml.dump(loaded_example, allow_unicode=True, sort_keys=False)


def highlight_yaml_example(example_text: str) -> str:
    """Filter. Return a highlighted YAML version of the provided JSON text"""
    return highlight(yaml_example(example_text), YamlLexer(), HtmlFormatter())
