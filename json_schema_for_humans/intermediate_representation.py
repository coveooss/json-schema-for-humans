import copy
import json
import os
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, TextIO, Tuple, Union

import requests
import yaml

from json_schema_for_humans import const
from json_schema_for_humans.jinja_filters import escape_property_name_for_id
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from json_schema_for_humans.schema_node import SchemaNode


def build_intermediate_representation(
    schema_path: Union[str, TextIO],
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

    def _resolve_ref(
        current_node: SchemaNode, schema: Union[Dict, List, int, str]
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
            that node. Otherwise "links_to" is the same as "refers_to". "refers_to" is the reference that was found.
        """
        if not isinstance(schema, Dict) or const.REF not in schema:
            return None, None

        reference_path = schema.get(const.REF)
        if not reference_path:
            return None, None

        # Reference found, resolve the path (format "#/a/b/c", "file.json#/a/b/c", or "file.json")
        if "#" not in reference_path:
            uri_part = reference_path
            anchor_part = ""
        else:
            uri_part, anchor_part = reference_path.split("#", maxsplit=1)
            anchor_part = anchor_part.strip("/")

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

        def _find_reference(path: str, anchor_path: str) -> Optional[SchemaNode]:
            resolved_references_for_this_schema = resolved_references[path]
            return resolved_references_for_this_schema.get(anchor_path)

        # Check if already loaded
        found_reference = _find_reference(referenced_schema_path, anchor_part)

        if found_reference == current_node:
            found_reference = None

        if found_reference:
            reference_users_for_this_schema = reference_users[found_reference.file][anchor_part]
            reference_users[referenced_schema_path][anchor_part].append(current_node)

            # Detect infinite loop
            ref_by_file = current_node.file
            ref_by_path = current_node.flat_path
            found_users = reference_users.get(ref_by_file, {}).get(ref_by_path)
            while found_users:
                new_found_users = []
                for found_user in found_users:
                    if found_user == current_node:
                        # Huh oh, this node refers to the current node, let's break the cycle!
                        return None, None
                    ref_by_file = found_user.file
                    ref_by_path = found_user.flat_path
                    found_users_for_this = reference_users.get(ref_by_file, {}).get(ref_by_path)
                    if found_users_for_this:
                        new_found_users += found_users_for_this
                found_users = new_found_users

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
                    # The current node will documented the element referenced by both
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
        else:
            reference_users[referenced_schema_path][anchor_part].append(current_node)

        # Not an existing reference, so it shall be built
        referenced_schema_path_to_element = anchor_part.split("/")
        new_reference = _build_node(
            current_node.depth,
            current_node.html_id,
            current_node.breadcrumb_name,
            referenced_schema_path,
            referenced_schema_path_to_element,
            _load_schema(referenced_schema_path, referenced_schema_path_to_element),
            current_node.parent,
            current_node.parent_key,
        )
        return new_reference, new_reference

    def _load_schema(schema_uri: str, path_to_element: List[Union[str, int]]) -> Union[Dict, List, int, str]:
        """Load the schema at the provided path or URL.

        If the URI is for a local file, it must be a "realpath", meaning absolute and with symlinks resolved.

        Loaded paths are kept in memory as to ensure never loading the same file twice
        """
        if schema_uri in _loaded_schemas:
            loaded_schema = _loaded_schemas[schema_uri]
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
            _loaded_schemas[schema_uri] = loaded_schema

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
                    loaded_schema = loaded_schema[path_part]

        return loaded_schema

    def _get_node_ref(schema: Union[int, str, List, Dict]) -> str:
        if isinstance(schema, dict) and const.REF in schema:
            return schema[const.REF]
        return ""

    def _build_node(
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

        _record_ref(schema_file_path, path_to_element, new_node)

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

                if schema_key in const.KW_PROPERTIES:
                    for new_property_name, new_property_schema in schema_value.items():
                        new_html_id = html_id
                        new_html_id += "_" if html_id else ""
                        new_html_id += escape_property_name_for_id(new_property_name)
                        new_node.properties[new_property_name] = _build_node(
                            depth + 1,
                            new_html_id,
                            new_property_name,
                            schema_file_path,
                            copy.deepcopy(path_to_element) + [new_property_name],
                            new_property_schema,
                            new_node,
                            new_property_name,
                        )
                elif schema_key == const.KW_ADDITIONAL_PROPERTIES:
                    if schema_value == False:
                        new_node.no_additional_properties = True
                    else:
                        new_html_id = html_id
                        new_html_id += "_" if html_id else ""
                        new_html_id += const.KW_ADDITIONAL_PROPERTIES
                        new_node.additional_properties = _build_node(
                            depth + 1,
                            new_html_id,
                            const.KW_ADDITIONAL_PROPERTIES,
                            schema_file_path,
                            copy.deepcopy(path_to_element) + [const.KW_ADDITIONAL_PROPERTIES],
                            schema_value,
                            new_node,
                            const.KW_ADDITIONAL_PROPERTIES,
                        )
                elif schema_key == const.KW_PATTERN_PROPERTIES:
                    for new_property_name, new_property_schema in schema_value.items():
                        new_html_id = html_id
                        new_html_id += "_" if html_id else ""
                        new_html_id += f"pattern{pattern_id}"
                        pattern_id += 1
                        new_node.pattern_properties[new_property_name] = _build_node(
                            depth + 1,
                            new_html_id,
                            new_property_name,
                            schema_file_path,
                            copy.deepcopy(path_to_element) + [new_property_name],
                            new_property_schema,
                            new_node,
                            new_property_name,
                        )
                else:
                    # Add the property name (correctly escaped) to the ID
                    new_html_id = html_id
                    new_depth = depth
                    if schema_key not in [const.KW_PROPERTIES, const.KW_PATTERN_PROPERTIES]:
                        new_depth += 1
                        new_html_id += "_" if html_id else ""
                        if not parent_key == const.KW_PATTERN_PROPERTIES:
                            new_html_id += escape_property_name_for_id(schema_key)
                        else:
                            new_html_id += f"pattern{pattern_id}"
                            pattern_id += 1

                    keywords[schema_key] = _build_node(
                        new_depth,
                        new_html_id,
                        schema_key,
                        schema_file_path,
                        copy.deepcopy(path_to_element) + [schema_key],
                        schema_value,
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
                        depth + 1,
                        new_html_id,
                        f"item {i}",
                        schema_file_path,
                        path_to_element + [i],
                        element,
                        parent=new_node,
                    )
                )
            new_node.array_items = array_items

        else:
            new_node.literal = schema

        new_node.links_to, new_node.refers_to = _resolve_ref(new_node, schema)

        return new_node

    intermediate_representation = _build_node(0, "", "root", schema_path, [], _load_schema(schema_path, []))

    return intermediate_representation
