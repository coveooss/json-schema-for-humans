import re
import json
import yaml
from datetime import datetime
from typing import List, Any

from jinja2 import pass_environment, Environment
from markdown2 import Markdown
from markupsafe import Markup
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.data import YamlLexer
from pytz import reference

from json_schema_for_humans import const
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from json_schema_for_humans.schema.schema_node import SchemaNode

SHORT_DESCRIPTION_NUMBER_OF_LINES = 8
DEFAULT_PATTERN = r"(\[Default - `([^`]+)`\])"
DEPRECATED_PATTERN = r"\[Deprecated"


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

    return bool(re.match(DEPRECATED_PATTERN, schema_node.keywords[const.DESCRIPTION].literal))


def get_required_properties(schema_node: SchemaNode) -> List[str]:
    required_properties = schema_node.keywords.get("required") or []
    if required_properties:
        required_properties = [p.literal for p in required_properties.array_items]

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
    return json.dumps(value, indent=4, separators=(",", ": "), ensure_ascii=False)


@pass_environment
def get_description(env: Environment, schema_node: SchemaNode) -> str:
    """Filter. Get the description of a property or an empty string"""
    description = schema_node.description

    config: GenerationConfiguration = env.globals["jsfh_config"]
    if config.default_from_description:
        match = re.match(DEFAULT_PATTERN, description)
        if match:
            description = description[match.span(1)[1] :].lstrip()

    if description and config.description_is_markdown and not config.result_extension == "md":
        # Markdown templates are expected to already have Markdown descriptions
        md: Markdown = env.globals["jsfh_md"]
        description = Markup(md.convert(description))

    return description


def get_default(schema_node: SchemaNode) -> str:
    """Filter. Return the default value for a property"""
    return schema_node.default_value


def get_default_look_in_description(schema_node: SchemaNode) -> str:
    """Filter. Get the default value of a JSON Schema property. If not set, look for it in the description."""
    default_value = schema_node.default_value
    if default_value:
        return default_value

    description = schema_node.keywords.get(const.DESCRIPTION)
    if not description:
        return ""
    description = description.literal

    match = re.match(DEFAULT_PATTERN, description)
    if not match:
        return ""

    return match.group(2)


def get_numeric_restrictions_text(schema_node: SchemaNode, before_value: str = "", after_value: str = "") -> str:
    """Filter. Get the text to display about restrictions on a numeric type(integer or number)"""
    multiple_of = schema_node.keywords.get(const.MULTIPLE_OF)
    if multiple_of:
        multiple_of = multiple_of.literal
    maximum = schema_node.keywords.get(const.MAXIMUM)
    if maximum:
        maximum = maximum.literal
    exclusive_maximum = schema_node.keywords.get(const.EXCLUSIVE_MAXIMUM)
    if exclusive_maximum:
        exclusive_maximum = exclusive_maximum.literal
    minimum = schema_node.keywords.get(const.MINIMUM)
    if minimum:
        minimum = minimum.literal
    exclusive_minimum = schema_node.keywords.get(const.EXCLUSIVE_MINIMUM)
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

    escaped = re.sub("[^0-9a-zA-Z_-]", "_", str(property_name))
    if not escaped[0].isalpha():
        escaped = "a" + escaped
    return escaped


def deprecated(config, schema: SchemaNode) -> bool:
    return is_deprecated_look_in_description(schema) if config.deprecated_from_description else is_deprecated(schema)


def first_line(example_text: str, max_length: int = 0) -> str:
    """Filter. Retrieve first line of string + add ... at the end if text has multiple lines cut line at max_length"""
    lines = example_text.splitlines()
    result = lines[0]
    etc = (max_length and len(result) > max_length) or len(lines) > 1
    return f"{result[:max_length]}{' ...' if etc else ''}"


def get_local_time() -> str:
    return datetime.now(tz=reference.LocalTimezone()).strftime("%Y-%m-%d at %H:%M:%S %z")


def highlight_json_example(example_text: str) -> str:
    """Filter. Return an highlighted version of the provided JSON text"""
    return highlight(example_text, JavascriptLexer(), HtmlFormatter())


def yaml_example(example_text: str) -> str:
    """Filter. Return a YAML version of the provided JSON text"""
    yaml_text = yaml.dump(json.loads(example_text), allow_unicode=True)
    return yaml_text


def highlight_yaml_example(example_text: str) -> str:
    """Filter. Return a highlighted YAML version of the provided JSON text"""
    return highlight(yaml_example(example_text), YamlLexer(), HtmlFormatter())
