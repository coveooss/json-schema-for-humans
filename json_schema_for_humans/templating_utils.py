from typing import TYPE_CHECKING, List, Optional, Type, Union

from json_schema_for_humans import const
from json_schema_for_humans.schema.schema_keyword import SchemaKeyword

if TYPE_CHECKING:
    from json_schema_for_humans.schema.schema_node import SchemaNode


def schema_keyword_to_int(schema_node: "SchemaNode", keyword: str) -> Optional[int]:
    """Extract an integer from a schema keyword"""
    keyword_value = schema_node.keywords.get(keyword)
    if keyword_value:
        keyword_value_literal = keyword_value.literal
        if isinstance(keyword_value_literal, int):
            return keyword_value_literal
    return None


def schema_keyword_to_str(schema_node: "SchemaNode", keyword: str) -> Optional[str]:
    """Extract a str from a schema keyword or return None"""
    keyword_value = schema_node.keywords.get(keyword)
    if keyword_value:
        keyword_value_literal = keyword_value.literal
        if isinstance(keyword_value_literal, str):
            return keyword_value_literal
    return None


def schema_keyword_lookup_to_str(schema_node: "SchemaNode", keyword: SchemaKeyword) -> Optional[str]:
    """Look up the str value of a schema keyword or return None

    If the keyword is not found on the given node, follow referenced nodes until
    the keyword is found. Returns None if the keyword is not found or is not a
    literal str.
    """
    value = schema_keyword_to_str(schema_node, keyword.value)

    seen = set()
    current_node = schema_node
    while not value and current_node.refers_to:
        if current_node in seen:
            break
        seen.add(current_node)
        referenced_schema = current_node.refers_to
        referenced_keyword_node = referenced_schema.keywords.get(keyword.value)
        if referenced_keyword_node:
            value = referenced_keyword_node.literal_str
        current_node = referenced_schema

    return value


def schema_keyword_convert_to_str(schema_node: "SchemaNode", keyword: str) -> Optional[str]:
    """Extract and convert to str from a schema keyword or return None"""
    keyword_value = schema_node.keywords.get(keyword)
    if keyword_value:
        return str(keyword_value.literal)
    return None


def get_type_name(schema_node: "SchemaNode") -> Optional[str]:
    """Filter. Return the type of a property taking into account the type of items for array and enum"""

    def _python_type_to_json_type(python_type: Type[Union[str, int, float, bool, list, dict, None]]) -> str:
        return {
            str: const.TYPE_STRING,
            int: const.TYPE_INTEGER,
            float: const.TYPE_NUMBER,
            bool: const.TYPE_BOOLEAN,
            list: const.TYPE_ARRAY,
            dict: const.TYPE_OBJECT,
            type(None): const.TYPE_NULL,
        }.get(python_type, const.TYPE_STRING)

    def _enum_type(enum_values: List["SchemaNode"]) -> str:
        enum_type_names = [
            _python_type_to_json_type(python_type_name)
            for python_type_name in set(type(v.literal) for v in enum_values)
        ]
        if enum_type_names:
            return f"{const.TYPE_ENUM} (of {' or '.join(sorted(enum_type_names))})"

        return const.TYPE_ENUM

    def _add_subtype_if_array(type_name: str):
        if type_name == const.TYPE_ARRAY:
            items = schema_node.array_items_def
            if not items:
                return type_name

            subtype_node = items.keywords.get(const.TYPE)
            subtype: Optional[str] = None
            if subtype_node:
                subtype = subtype_node.literal_str
            if const.TYPE_ENUM in items.keywords:
                subtype = _enum_type(items.keywords[const.TYPE_ENUM].array_items)

            if not subtype:
                # Too complex to guess items
                return type_name

            type_name = f"{type_name} of {subtype}"

        return type_name

    if schema_node.is_const:
        return const.TYPE_CONST
    if const.TYPE_ENUM in schema_node.keywords:
        return _enum_type(schema_node.keywords[const.TYPE_ENUM].array_items)

    type_node = schema_node.keywords.get(const.TYPE)
    type_names: List[str] = []
    if type_node:
        if isinstance(type_node, str):
            type_names = [type_node]
        elif type_node.array_items:
            type_names = [node.literal_str for node in type_node.array_items if node.literal_str]
        elif type_node.literal_str:
            type_names = [type_node.literal_str]
    else:
        return None

    if not type_names:
        return None

    type_names = [_add_subtype_if_array(type_name) for type_name in type_names]

    return ", ".join(type_names[:-1]) + (" or " if len(type_names) > 1 else "") + type_names[-1]
