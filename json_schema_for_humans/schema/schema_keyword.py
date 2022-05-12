from enum import Enum


class SchemaKeyword(Enum):
    REQUIRED = "required"
    TITLE = "title"
    CONTAINS = "contains"
    EXAMPLES = "examples"
    ITEMS = "items"
    PREFIX_ITEMS = "prefixItems"
    UNIQUE_ITEMS = "uniqueItems"
    ADDITIONAL_ITEMS = "additionalItems"
    MAX_ITEMS = "maxItems"
    MIN_ITEMS = "minItems"
    MAX_LENGTH = "maxLength"
    MIN_LENGTH = "minLength"
    PATTERN = "pattern"
    CONST = "const"
    ENUM = "enum"
    ELSE = "else"
    THEN = "then"
    IF = "if"
    NOT = "not"
    ONE_OF = "oneOf"
    ANY_OF = "anyOf"
    ALL_OF = "allOf"
    PROPERTIES = "properties"
    PATTERN_PROPERTIES = "patternProperties"
    ADDITIONAL_PROPERTIES = "additionalProperties"
    FORMAT = "format"
