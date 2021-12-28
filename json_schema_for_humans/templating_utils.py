from typing import List, Optional, Type, Union, TYPE_CHECKING

from json_schema_for_humans import const

if TYPE_CHECKING:
    from json_schema_for_humans.schema.schema_node import SchemaNode


def get_type_name(schema_node: "SchemaNode") -> Optional[str]:
    """Filter. Return the type of a property taking into account the type of items for array and enum"""

    def _python_type_to_json_type(python_type: Type[Union[str, int, float, bool, list, dict]]) -> str:
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
            return f"{const.TYPE_ENUM} (of {' or '.join(enum_type_names)})"

        return const.TYPE_ENUM

    def _add_subtype_if_array(type_name: str):
        if type_name == const.TYPE_ARRAY:
            items = schema_node.array_items_def
            if not items:
                return type_name

            subtype = items.keywords.get(const.TYPE)
            if subtype:
                subtype = subtype.literal
            if const.TYPE_ENUM in items.keywords:
                subtype = _enum_type(items.keywords[const.TYPE_ENUM].array_items)

            if not subtype:
                # Too complex to guess items
                return type_name

            type_name = f"{type_name} of {subtype}"

        return type_name

    if const.TYPE_CONST in schema_node.keywords:
        return const.TYPE_CONST
    if const.TYPE_ENUM in schema_node.keywords:
        return _enum_type(schema_node.keywords[const.TYPE_ENUM].array_items)

    type_node = schema_node.keywords.get(const.TYPE)
    if type_node:
        if isinstance(type_node, str):
            type_names = [type_node]
        elif type_node.array_items:
            type_names = [node.literal for node in type_node.array_items]
        else:
            type_names = [type_node.literal]
    else:
        return None

    type_names = [_add_subtype_if_array(type_name) for type_name in type_names]

    return ", ".join(type_names[:-1]) + (" or " if len(type_names) > 1 else "") + type_names[-1]
