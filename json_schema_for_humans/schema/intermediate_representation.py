import copy
import json
import os
import urllib.parse
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import requests
import yaml

from json_schema_for_humans import const
from json_schema_for_humans.const import FileLikeType
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from json_schema_for_humans.jinja_filters import escape_property_name_for_id
from json_schema_for_humans.schema.schema_keyword import SchemaKeyword
from json_schema_for_humans.schema.schema_node import SchemaNode

ROOT_ID = "__root__"


def build_intermediate_representation(
    schema_path: Union[str, Path, FileLikeType],
    config: GenerationConfiguration,
    loaded_schemas: Optional[Dict[str, Any]] = None,
) -> SchemaNode:
    """Build a SchemaNode object representing a JSON schema with added metadata to help rendering as a documentation.

    The representation will resolve references and generate HTML ids for elements
    """
    resolved_references: Dict[str, Dict[str, SchemaNode]] = defaultdict(dict)

    def defaultdict_list() -> Dict[Any, List]:
        return defaultdict(list)

    reference_users: Dict[str, Dict[str, List[SchemaNode]]] = defaultdict(defaultdict_list)
    loaded_schemas = loaded_schemas or {}

    # Make sure schema_path is absolute, all symlinks are resolved
    absolute_schema_path = _get_schema_path(schema_path)

    intermediate_representation = _build_node(
        config,
        resolved_references,
        reference_users,
        loaded_schemas,
        0,
        "",
        "root",
        absolute_schema_path,
        [],
        _load_schema(absolute_schema_path, [], loaded_schemas),
    )

    return intermediate_representation


def _record_ref(
    resolved_references: Dict[str, Dict[str, SchemaNode]],
    schema_real_path: str,
    path_to_element: List[Union[str, int]],
    current_node: SchemaNode,
) -> None:
    """Record that the node is describing the schema at the provided path"""
    path_to_element_str = "/".join(str(e) for e in path_to_element)
    resolved_references[schema_real_path][path_to_element_str] = current_node


def _has_recursive_reference(reference_users: Dict[str, Dict[str, List[SchemaNode]]], current_node: SchemaNode) -> bool:
    ref_by_file = current_node.file
    ref_by_path = current_node.flat_path
    found_users = reference_users.get(ref_by_file, {}).get(ref_by_path)
    while found_users:
        new_found_users = []
        for found_user in found_users:
            if found_user == current_node:
                return True
            ref_by_file = found_user.file
            ref_by_path = found_user.flat_path
            found_users_for_this = reference_users.get(ref_by_file, {}).get(ref_by_path)
            if found_users_for_this:
                new_found_users += found_users_for_this
        found_users = new_found_users
    return False


def _has_reference_to_parent(referenced_schema_path: str, anchor_part: str, current_node: SchemaNode) -> bool:
    if referenced_schema_path != current_node.file:
        return False
    split_anchor_part = anchor_part.split("/")
    if len(split_anchor_part) > len(current_node.path_to_element):
        return False
    for i in range(len(split_anchor_part)):
        if split_anchor_part[i] != current_node.path_to_element[i]:
            return False
    return True


def _find_ref(
    found_reference: SchemaNode,
    referenced_schema_path: str,
    reference_users: Dict[str, Dict[str, List[SchemaNode]]],
    resolved_references: Dict[str, Dict[str, SchemaNode]],
    anchor_part: str,
    current_node: SchemaNode,
) -> Tuple[Optional[SchemaNode], Optional[SchemaNode]]:
    reference_users_for_this_schema = reference_users[found_reference.file][anchor_part]

    # Detect infinite loop
    if _has_recursive_reference(reference_users, current_node):
        # Huh oh, this node refers to the current node, let's break the cycle!
        return None, None

    # Check if the node has already been documented (also for infinite loops)
    already_resolved = resolved_references.get(referenced_schema_path, {}).get(anchor_part, {})
    if already_resolved:
        # The node is already documented elsewhere. Let's link to it
        current_node.is_displayed = False
        return already_resolved, already_resolved

    # Find the first displayed node following the references
    while not found_reference.is_displayed and found_reference.refers_to:
        if found_reference.refers_to == current_node:
            break
        found_reference = found_reference.refers_to

    # Is someone else using the reference?
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

        # There is at least one other node having the same reference as the current node.
        if other_is_better:
            # The other referencing node is nearer to the user, so it will now be displayed
            # We mark the current node as being hidden and linking to the other one
            other_user.is_displayed = True
            current_node.is_displayed = False
            return other_user, found_reference
        elif i_am_better:
            # The other referencing node is more nested, it should be hidden and link to the current node
            # The current node will document the element referenced by both
            other_user.is_displayed = False
            other_user.links_to = current_node
            current_node.is_displayed = True
            return found_reference, found_reference
        elif other_user and other_user.refers_to:
            # Both nodes are the same depth. The other having been seen first,
            # this node will be hidden and linked to the other node
            current_node.is_displayed = False
            return other_user, found_reference

    return found_reference, found_reference


def _resolve_ref(
    config: GenerationConfiguration,
    resolved_references: Dict[str, Dict[str, SchemaNode]],
    reference_users: Dict[str, Dict[str, List[SchemaNode]]],
    current_node: SchemaNode,
    schema: Union[Dict, List, int, str],
    loaded_schemas: Dict[str, Any],
) -> Tuple[Optional[SchemaNode], Optional[SchemaNode]]:
    """Resolve the $ref keyword

    2 values are returned:
     - The "links_to" value, which is the node to which the current node should point to. This is used when several
       nodes have the same reference.

       This value cannot be under #/definitions, since those are not displayed.

       If properties a and b both references #/definitions/common, only a will be documented and b will link to a.
       In that case, the method would return the tuple (a, common).

       This method makes sure that the final element to be fully documented is the one that is the less nested so
       that the information is closer to the user.
       If properties a/b and c both references #/definitions/common, then a/b will link to c (c, common) and c will
       refer to common directly (None, common)
    - The "refers_to" value which is where the definition is in the schema.

    In general:
    - If there is no $ref, return (None, None).
    - If there is a referenced element that was never encountered before, build that element and return it for both
      "links_to" and "refers_to".
    - If there is a referenced element that was already encountered:
      - Check for circular references, if there are, return (None, None)
      - Check if another built node references the same one. If that node is closer to the user, "links_to" will be
        that node. Otherwise, "links_to" is the same as "refers_to". "refers_to" is the reference that was found.
    """
    if not isinstance(schema, Dict) or const.REF not in schema:
        return None, None

    reference_path = schema.get(const.REF)
    if not reference_path:
        return None, None

    # Reference found, resolve the path (format "#/a/b/c", "file.json#/a/b/c", or "file.json")
    if "#" not in reference_path:
        uri_part = reference_path
        anchor_part = ROOT_ID
    else:
        uri_part, anchor_part = reference_path.split("#", maxsplit=1)
        anchor_part = urllib.parse.unquote(anchor_part)
        anchor_part = anchor_part.strip("/") or ROOT_ID  # Special case for the root schema

    # Resolve file path portion of reference
    if uri_part:
        if uri_part.startswith("http"):
            referenced_schema_path = uri_part
        else:
            referenced_schema_path = os.path.realpath(os.path.join(os.path.dirname(current_node.file), uri_part))
    elif current_node.file.startswith("http"):
        referenced_schema_path = current_node.file
    else:
        referenced_schema_path = os.path.realpath(current_node.file)

    # Check if already loaded
    found_reference = resolved_references[referenced_schema_path].get(anchor_part)
    reference_users[referenced_schema_path][anchor_part].append(current_node)

    if found_reference and found_reference != current_node:
        if config.link_to_reused_ref:
            return _find_ref(
                found_reference,
                referenced_schema_path,
                reference_users,
                resolved_references,
                anchor_part,
                current_node,
            )
        else:
            if _has_recursive_reference(reference_users, current_node) or _has_reference_to_parent(
                referenced_schema_path, anchor_part, current_node
            ):
                current_node.is_displayed = False
                return found_reference, found_reference

    # Not an existing reference, so it shall be built
    referenced_schema_path_to_element = anchor_part.split("/")
    new_reference = _build_node(
        config,
        resolved_references,
        reference_users,
        loaded_schemas,
        current_node.depth,
        current_node.html_id,
        current_node.breadcrumb_name,
        referenced_schema_path,
        referenced_schema_path_to_element,
        _load_schema(referenced_schema_path, referenced_schema_path_to_element, loaded_schemas),
        current_node.parent,
        current_node.parent_key,
    )
    return new_reference, new_reference


def _get_schema_path(schema_path: Union[str, Path, FileLikeType]) -> str:
    if isinstance(schema_path, Path):
        return str(schema_path.resolve())
    elif isinstance(schema_path, str):
        return os.path.realpath(schema_path)
    else:
        return os.path.realpath(schema_path.name)


def _get_node_ref(schema: Union[int, str, List, Dict]) -> str:
    if isinstance(schema, dict) and const.REF in schema:
        return schema[const.REF]
    return ""


def _load_schema_from_uri(schema_uri: str, loaded_schemas: Dict[str, Any]):
    if schema_uri in loaded_schemas:
        loaded_schema = loaded_schemas[schema_uri]
    else:
        if schema_uri.startswith("http"):
            if schema_uri.endswith(".yaml"):
                loaded_schema = yaml.safe_load(requests.get(schema_uri).text)
            else:
                loaded_schema = requests.get(schema_uri).json()
        else:
            with open(schema_uri, encoding="utf-8") as schema_fp:
                _, extension = os.path.splitext(schema_uri)
                if extension == ".json":
                    loaded_schema = json.load(schema_fp)
                else:
                    loaded_schema = yaml.safe_load(schema_fp)
        loaded_schemas[schema_uri] = loaded_schema

    return loaded_schema


def _load_schema(
    schema_uri: str, path_to_element: List[Union[str, int]], loaded_schemas: Dict[str, Any]
) -> Union[Dict, List, int, str]:
    """Load the schema at the provided path or URL.

    If the URI is for a local file, it must be a "realpath", meaning absolute and with symlinks resolved.

    Loaded paths are kept in memory as to ensure never loading the same file twice
    """
    loaded_schema = _load_schema_from_uri(schema_uri, loaded_schemas)

    if path_to_element:
        for path_part in path_to_element:
            if not path_part:
                # Empty string
                continue
            try:
                path_part_int = int(path_part)
                loaded_schema = loaded_schema[path_part_int]
                continue
            except (KeyError, ValueError):
                # KeyError: The part looks like a int but it is a string (property named "0" for example
                # ValueError: Normal case, the path part is a string
                if path_part == ROOT_ID:
                    return loaded_schema
                loaded_schema = loaded_schema[path_part]

    return loaded_schema


def _build_node(
    config: GenerationConfiguration,
    resolved_references: Dict[str, Dict[str, SchemaNode]],
    reference_users: Dict[str, Dict[str, List[SchemaNode]]],
    loaded_schemas: Dict[str, Any],
    depth: int,
    html_id: str,
    breadcrumb_name: str,
    schema_file_path: str,
    path_to_element: List[Union[str, int]],
    schema: Union[Dict, List, int, str],
    parent: Optional[SchemaNode] = None,
    parent_key: Optional[str] = None,
) -> SchemaNode:
    """Recursively build a schema representation

    :param depth: Number of levels from the root of the schema to this node. Used when there are references to
                  figure out the less nested one in order to display it.
    :param html_id: HTML ID for the current element. Used for anchor links.
    :param breadcrumb_name: Name of the node in the breadcrumbs
    :param schema_file_path: Real path to the schema (absolute path with symlinks resolved)
    :param path_to_element: Path from the root of the schema to the current element
    :param schema: The JSON schema part being represented
    :return: A representation of the schema
    """
    if not schema_file_path.startswith("http"):
        schema_file_path = os.path.realpath(schema_file_path)

    new_node = SchemaNode(
        depth,
        file=schema_file_path,
        path_to_element=path_to_element,
        html_id=html_id,
        breadcrumb_name=breadcrumb_name,
        parent=parent,
        parent_key=parent_key,
        ref_path=_get_node_ref(schema),
    )
    if html_id == "root":
        html_id = ""
    if not path_to_element:
        path_to_element = [ROOT_ID]

    _record_ref(resolved_references, schema_file_path, path_to_element, new_node)

    if isinstance(schema, dict):
        keywords = {}
        pattern_id = 1
        for schema_key, schema_value in schema.items():
            # These won't be needed to render the documentation.
            # The definitions will be reached from references, otherwise they are useless
            if schema_key in ["$id", "$ref", "$schema", "definitions"]:
                continue

            # Examples are rendered in JSON because they will be represented that way in the documentation,
            # no need for a SchemaNode object
            if schema_key == SchemaKeyword.EXAMPLES.value:
                keywords[schema_key] = [
                    json.dumps(example, indent=4, separators=(",", ": "), ensure_ascii=False)
                    for example in schema_value
                ]
                continue

            # The default value will be printed as-is, no need for a SchemaNode object
            if schema_key == "default":
                keywords[schema_key] = json.dumps(schema_value, ensure_ascii=False)
                continue

            if schema_key == SchemaKeyword.PROPERTIES.value:
                for new_property_name, new_property_schema in schema_value.items():
                    new_html_id = html_id
                    new_html_id += "_" if html_id else ""
                    new_html_id += escape_property_name_for_id(new_property_name)
                    new_node.properties[new_property_name] = _build_node(
                        config=config,
                        resolved_references=resolved_references,
                        reference_users=reference_users,
                        loaded_schemas=loaded_schemas,
                        depth=depth + 1,
                        html_id=new_html_id,
                        breadcrumb_name=new_property_name,
                        schema_file_path=schema_file_path,
                        path_to_element=copy.deepcopy(path_to_element) + [new_property_name],
                        schema=new_property_schema,
                        parent=new_node,
                        parent_key=new_property_name,
                    )
            elif schema_key == SchemaKeyword.ADDITIONAL_PROPERTIES.value:
                if schema_value is False:
                    new_node.no_additional_properties = True
                else:
                    new_html_id = html_id
                    new_html_id += "_" if html_id else ""
                    new_html_id += SchemaKeyword.ADDITIONAL_PROPERTIES.value
                    new_node.additional_properties = _build_node(
                        config=config,
                        resolved_references=resolved_references,
                        reference_users=reference_users,
                        loaded_schemas=loaded_schemas,
                        depth=depth + 1,
                        html_id=new_html_id,
                        breadcrumb_name=SchemaKeyword.ADDITIONAL_PROPERTIES.value,
                        schema_file_path=schema_file_path,
                        path_to_element=copy.deepcopy(path_to_element) + [SchemaKeyword.ADDITIONAL_PROPERTIES.value],
                        schema=schema_value,
                        parent=new_node,
                        parent_key=SchemaKeyword.ADDITIONAL_PROPERTIES.value,
                    )
            elif schema_key == SchemaKeyword.PATTERN_PROPERTIES.value:
                for new_property_name, new_property_schema in schema_value.items():
                    new_html_id = html_id
                    new_html_id += "_" if html_id else ""
                    new_html_id += f"pattern{pattern_id}"
                    pattern_id += 1
                    new_node.pattern_properties[new_property_name] = _build_node(
                        config=config,
                        resolved_references=resolved_references,
                        reference_users=reference_users,
                        loaded_schemas=loaded_schemas,
                        depth=depth + 1,
                        html_id=new_html_id,
                        breadcrumb_name=new_property_name,
                        schema_file_path=schema_file_path,
                        path_to_element=copy.deepcopy(path_to_element) + [new_property_name],
                        schema=new_property_schema,
                        parent=new_node,
                        parent_key=new_property_name,
                    )
            elif schema_key in [SchemaKeyword.ITEMS.value, SchemaKeyword.PREFIX_ITEMS.value]:
                if isinstance(schema_value, list):
                    # Tuple validation
                    # https://json-schema.org/understanding-json-schema/reference/array.html#tuple-validation
                    for i, array_item_schema in enumerate(schema_value):
                        item_breadcrumb_name = f"{breadcrumb_name} item {i}"
                        new_node.tuple_validation_items.append(
                            _build_node(
                                config=config,
                                resolved_references=resolved_references,
                                reference_users=reference_users,
                                loaded_schemas=loaded_schemas,
                                depth=depth + 1,
                                html_id=f"{html_id}_items_i{i}",
                                breadcrumb_name=item_breadcrumb_name,
                                schema_file_path=schema_file_path,
                                path_to_element=copy.deepcopy(path_to_element) + [item_breadcrumb_name],
                                schema=array_item_schema,
                                parent=new_node,
                                parent_key=schema_key,
                            )
                        )
                else:
                    breadcrumb_name = f"{breadcrumb_name} items"
                    new_node.array_items_def = _build_node(
                        config=config,
                        resolved_references=resolved_references,
                        reference_users=reference_users,
                        loaded_schemas=loaded_schemas,
                        depth=depth + 1,
                        html_id=f"{html_id}_items",
                        breadcrumb_name=breadcrumb_name,
                        schema_file_path=schema_file_path,
                        path_to_element=copy.deepcopy(path_to_element) + [breadcrumb_name],
                        schema=schema_value,
                        parent=new_node,
                        parent_key=schema_key,
                    )
            else:
                # Add the property name (correctly escaped) to the ID
                new_html_id = html_id
                new_depth = depth
                if schema_key not in [SchemaKeyword.PROPERTIES.value, SchemaKeyword.PATTERN_PROPERTIES.value]:
                    new_depth += 1
                    new_html_id += "_" if html_id else ""
                    if not parent_key == SchemaKeyword.PATTERN_PROPERTIES.value:
                        new_html_id += escape_property_name_for_id(schema_key)
                    else:
                        new_html_id += f"pattern{pattern_id}"
                        pattern_id += 1

                keywords[schema_key] = _build_node(
                    config=config,
                    resolved_references=resolved_references,
                    reference_users=reference_users,
                    loaded_schemas=loaded_schemas,
                    depth=new_depth,
                    html_id=new_html_id,
                    breadcrumb_name=schema_key,
                    schema_file_path=schema_file_path,
                    path_to_element=copy.deepcopy(path_to_element) + [schema_key],
                    schema=schema_value,
                    parent=new_node,
                    parent_key=schema_key,
                )
        new_node.keywords = keywords
    elif isinstance(schema, list):
        array_items = []
        for i, element in enumerate(schema):
            # Add the property name (correctly escaped) to the ID
            new_html_id = html_id + ("_" if html_id else "") + "i" + str(i)

            array_items.append(
                _build_node(
                    config=config,
                    resolved_references=resolved_references,
                    reference_users=reference_users,
                    loaded_schemas=loaded_schemas,
                    depth=depth + 1,
                    html_id=new_html_id,
                    breadcrumb_name=f"item {i}",
                    schema_file_path=schema_file_path,
                    path_to_element=path_to_element + [i],
                    schema=element,
                    parent=new_node,
                )
            )
        new_node.array_items = array_items

    else:
        new_node.literal = schema

    new_node.links_to, new_node.refers_to = _resolve_ref(
        config, resolved_references, reference_users, new_node, schema, loaded_schemas
    )

    return new_node
