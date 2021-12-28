import copy
from typing import Any, Dict, Iterable, Iterator, List, Optional, Set, Union, cast

from json_schema_for_humans import const
from json_schema_for_humans.schema.schema_keyword import SchemaKeyword
from json_schema_for_humans.templating_utils import get_type_name
from json_schema_for_humans.generation_configuration import GenerationConfiguration

circular_references: Dict["SchemaNode", bool] = {}


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
        breadcrumb_name: str = "",
        ref_path="",
        parent: "SchemaNode" = None,
        parent_key: str = None,
        literal: Optional[Union[str, int, bool]] = None,
        keywords: Dict[str, Union["SchemaNode", str, List[str]]] = None,
        array_items: List["SchemaNode"] = None,
        array_items_def: Optional["SchemaNode"] = None,
        tuple_validation_items: Optional[List["SchemaNode"]] = None,
        links_to: "SchemaNode" = None,
        refers_to: "SchemaNode" = None,
        is_displayed: bool = True,
    ):
        """

        :param depth: Number of levels from the root of the schema to this node.
        :param file: Real path to the schema file
        :param path_to_element: Path from the root of the schema to the current element
        :param html_id: HTML ID for the current element. Used for anchor links.
        :param parent: The parent node of which the current node is an array item or keyword
        :param parent_key: If the node is under a keyword of the parent node, that keyword
            Example:
            In the following context
            {
                "patternProperties": {
                    ".*": {
                        "type": string
                    }
                }
            }

            For the node
            {
                "type": string
            }
            The parent_key is ".*"

            For the node
            {
                ".*": {
                    "type": string
                }
            }
            The parent key is "patternProperties"

        :param ref_path: Path of a reference to this element, if any (usually "#/definitions/A name")
        :param literal: If the schema is neither a dict nor an array, it will be kept here
                        Useful for things like description, types, const, enum, etc.
        :param keywords: If the schema is a dict, this will be filled. Otherwise, this stays empty
        :param array_items: If the schema is an array, this will be filled. Otherwise, this stays empty
        :param array_items_def: Definition of the array items that this node can contain
        :param tuple_validation_items: Like array_items_def, but defined by position (i.e the element at position i in
                                       a JSON file respecting the schema must respect the schema at position i of this
                                       array)
        :param links_to: If the same node is documented elsewhere, the other SchemaNode that documents it
        :param refers_to: If there is a $ref, this should contain the SchemaNode object for it
        :param is_displayed: Instructs the templates if this part should be fully documented.
                             If false, the description and a link to the referenced element will be generated instead.
                             If false, refers_to needs to be set
        """
        self.depth = depth
        self.file = file
        self.path_to_element = path_to_element
        self.html_id = html_id or "_".join(path_to_element) or "root"
        self.breadcrumb_name = breadcrumb_name
        self.parent = parent
        self.parent_key = parent_key
        self.ref_path = ref_path
        self.literal = literal
        self.keywords = keywords or {}
        self.array_items = array_items or []
        self.links_to = links_to
        self.refers_to = refers_to
        self.is_displayed = is_displayed
        self._refers_to_merged = None
        self.properties: Dict[str, "SchemaNode"] = {}
        self.additional_properties: Optional["SchemaNode"] = None
        # If True, it means additionalProperties is there and false. If False, additionalProperties is either not set
        # or is set but is not false (depends on self.additional_properties)
        self.no_additional_properties: bool = False
        self.pattern_properties: Dict[str, "SchemaNode"] = {}
        self.array_items_def: Optional["SchemaNode"] = array_items_def
        self.tuple_validation_items: List["SchemaNode"] = tuple_validation_items or []

    @property
    def explicit_no_additional_properties(self) -> bool:
        """Return True if additionalProperties is set and false (to differentiate from not set)"""
        return bool(
            (self.properties or self.pattern_properties)
            and self.no_additional_properties
            and not self.additional_properties
        )

    @property
    def definition_name(self) -> str:
        """The text to display when this node is the title of a section or tab"""
        if self.is_property and self.property_name:
            return self.property_name
        if self.title:
            return self.title
        if self.ref_path:
            return self.ref_path.split("/")[-1]
        return ""

    @property
    def link_name(self) -> str:
        """The text to display when linking to this node from somewhere else in the schema"""
        return self.definition_name or self.html_id

    @property
    def name_for_breadcrumbs(self) -> str:
        return self.definition_name or self.breadcrumb_name

    @property
    def is_property(self) -> bool:
        return bool(self.parent and self.property_name in self.parent.properties.keys())

    @property
    def is_pattern_property(self) -> bool:
        return bool(self.parent and self.property_name in self.parent.pattern_properties.keys())

    @property
    def is_additional_properties(self) -> bool:
        return self.parent_key == SchemaKeyword.ADDITIONAL_PROPERTIES.value

    @property
    def is_a_property_node(self) -> bool:
        return self.is_property or self.is_pattern_property or self.is_additional_properties

    @property
    def is_additional_properties_schema(self) -> bool:
        return self.is_additional_properties and self.literal is not True

    @property
    def iterate_properties(self) -> Iterable["SchemaNode"]:
        if self.properties:
            yield from self.properties.values()

        if self.pattern_properties:
            yield from self.pattern_properties.values()

        if self.additional_properties:
            yield self.additional_properties

    @property
    def required_properties(self) -> List[str]:
        """The required properties for this node"""
        required_properties = self.kw_required
        if not required_properties:
            return []

        return [r.literal for r in required_properties.array_items]

    @property
    def is_required_property(self) -> bool:
        """Check if the current node represents a property and that this property is required by its parent"""
        return self.parent and self.property_name in self.parent.required_properties

    @property
    def nodes_from_root(self) -> Iterator["SchemaNode"]:
        """The list of nodes to reach this node"""
        nodes: List["SchemaNode"] = [self]
        current_node = self
        while current_node.parent:
            nodes.append(current_node.parent)
            current_node = current_node.parent

        if len(nodes) == 1:
            # Don't want to display "root" alone at the root
            return []

        return reversed(nodes)

    @property
    def path_to_property(self) -> str:
        """Human-readable representation of the path from the root of the schema to this node"""
        path_without_properties = [
            p
            for p in self.path_to_element
            if p not in [SchemaKeyword.PROPERTIES.value, SchemaKeyword.PATTERN_PROPERTIES.value]
        ]
        return " -> ".join([p if isinstance(p, str) else f"Item {p}" for p in path_without_properties])

    @property
    def flat_path(self) -> str:
        """String representation of the path to this node from the root of the current schema"""
        return "/".join(str(part) for part in self.path_to_element)

    @property
    def default_value(self) -> Optional[Any]:
        def _default_value(node: SchemaNode) -> Optional[Any]:
            default = node.keywords.get(const.DEFAULT)
            if isinstance(default, SchemaNode) and default.is_a_property_node:
                return None
            return default

        seen = set()
        current_node = self
        possible_default = _default_value(current_node)
        while not possible_default and current_node.refers_to:
            if current_node in seen:
                break
            seen.add(current_node)
            current_node = current_node.refers_to
            possible_default = _default_value(current_node)

        return possible_default

    @property
    def description(self) -> str:
        description = ""
        description_node = self.keywords.get(const.DESCRIPTION)
        if description_node:
            description = description_node.literal

        seen = set()
        current_node = self
        while not description and current_node.refers_to:
            if current_node in seen:
                break
            seen.add(current_node)
            referenced_schema = current_node.refers_to
            referenced_description_node = referenced_schema.keywords.get(const.DESCRIPTION)
            if referenced_description_node:
                description = referenced_description_node.literal
            current_node = referenced_schema

        return description

    @property
    def examples(self) -> List[str]:
        possible_examples = self.keywords.get(const.EXAMPLES)
        if not possible_examples:
            return []

        if isinstance(possible_examples, SchemaNode) and possible_examples.is_a_property_node:
            return []

        return possible_examples

    @property
    def refers_to_merged(self) -> Optional["SchemaNode"]:
        """The referenced node, with values from the current node merged in"""
        if self._refers_to_merged:
            return self._refers_to_merged

        if not self.refers_to:
            return None

        merged_node = copy.copy(self.refers_to)
        merged_node.keywords = {k: copy.copy(v) for k, v in self.refers_to.keywords.items()}
        merged_node.array_items = [copy.copy(i) for i in self.refers_to.array_items]

        merged_node.keywords.update({k: copy.copy(v) for k, v in self.keywords.items()})
        merged_node.array_items += [copy.copy(i) for i in self.array_items]

        return merged_node

        # self._refers_to_merged = merged_node

        # return self._refers_to_merged

    def get_keyword(self, keyword: SchemaKeyword) -> Optional["SchemaNode"]:
        """Get the value of a keyword if present and it is not a property (to avoid conflicts with properties being
        named like a keyword, e.g. a property named "if")
        """
        possible_keyword = self.keywords.get(keyword.value)
        if possible_keyword and isinstance(possible_keyword, SchemaNode) and not possible_keyword.is_property:
            return possible_keyword

        return None

    @property
    def kw_all_of(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.ALL_OF)

    @property
    def kw_any_of(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.ANY_OF)

    @property
    def kw_one_of(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.ONE_OF)

    @property
    def kw_not(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.NOT)

    @property
    def has_conditional(self) -> bool:
        return self.kw_if is not None and (self.kw_then is not None or self.kw_else is not None)

    @property
    def kw_if(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.IF)

    @property
    def kw_then(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.THEN)

    @property
    def kw_else(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.ELSE)

    @property
    def kw_enum(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.ENUM)

    @property
    def kw_const(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.CONST)

    @property
    def kw_pattern(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.PATTERN)

    @property
    def kw_properties(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.PROPERTIES)

    @property
    def kw_pattern_properties(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.PATTERN_PROPERTIES)

    @property
    def kw_additional_properties(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.ADDITIONAL_PROPERTIES)

    @property
    def kw_min_length(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.MIN_LENGTH)

    @property
    def kw_max_length(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.MAX_LENGTH)

    @property
    def kw_items(self) -> Optional[List["SchemaNode"]]:
        """items can be either an object either a list of object"""
        items = self.get_keyword(SchemaKeyword.ITEMS)
        if not items:
            return None

        if items.array_items:
            return items.array_items

        return [items]

    @property
    def kw_min_items(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.MIN_ITEMS)

    @property
    def kw_max_items(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.MAX_ITEMS)

    @property
    def kw_unique_items(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.UNIQUE_ITEMS)

    @property
    def kw_additional_items(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.ADDITIONAL_ITEMS)

    @property
    def kw_contains(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.CONTAINS)

    @property
    def kw_required(self) -> Optional["SchemaNode"]:
        return self.get_keyword(SchemaKeyword.REQUIRED)

    @property
    def title(self) -> Optional[str]:
        title_kw = self.get_keyword(SchemaKeyword.TITLE)
        if not title_kw:
            return None
        title = title_kw.literal
        title = cast(str, title)
        return title

    @property
    def property_name(self) -> Optional[str]:
        return self.parent_key

    @property
    def property_display_name(self) -> Optional[str]:
        """The name to display in documentation for this property.

        This is simply the property name unless it is under "patternProperties" and it has a title,
        in which case it is that title
        """
        if self.is_pattern_property:
            return self.title or self.parent_key
        if self.is_additional_properties:
            return "Additional Properties"
        return self.parent_key

    @property
    def type_name(self) -> str:
        name = get_type_name(self)

        if name:
            return name

        seen = set()
        current_node = self
        while not name and current_node.refers_to:
            if current_node in seen:
                break
            seen.add(current_node)
            referenced_schema = current_node.refers_to
            name = get_type_name(referenced_schema)
            current_node = referenced_schema

        return name or const.TYPE_OBJECT

    @property
    def raw(self) -> Optional[Union[int, bool, str, List, Dict]]:
        """Get the value of the node as it would exist in the original schema.
        Useful for const where we don't care for the structure and just want to display the value
        """
        if self.literal is not None:
            return self.literal
        if self.array_items:
            return [node.raw for node in self.array_items]
        if self.keywords:
            return {k: v.raw for k, v in self.keywords.items()}
        return None

    def should_be_a_link(self, config: GenerationConfiguration) -> bool:
        """Check if this node should be displayed as a link to another section of the schema in the context of
        the provided configuration.
        """
        if not self.links_to or self.is_displayed:
            return False

        if config.link_to_reused_ref:
            return True

        return self.has_circular_reference(config)

    def node_is_parent(self, node_to_check: "SchemaNode") -> bool:
        """Check if the provided node is a parent of the current node"""
        if self.file != node_to_check.file:
            return False

        for i, path_part in enumerate(node_to_check.path_to_element):
            if len(self.path_to_element) <= i:
                return False
            if self.path_to_element[i] != path_part:
                return False
        return True

    def has_circular_reference(self, config: GenerationConfiguration) -> bool:
        """Check if the current schema is a reference to another section that references the current schema.

        The check is recursive up to config.recursive_detection_depth levels, meaning that if the node refers to another
        node that refers to another node that refers to a parent of itself, this will still return True if, and only if,
        it takes less than config.recursive_detection_depth steps to get to the parent.
        """
        if self in circular_references:
            return circular_references[self]

        if not self.links_to:
            circular_references[self] = False
            return False

        iteration_count = 0
        to_check = {self.links_to}
        while to_check and iteration_count < config.recursive_detection_depth:
            for node_to_check in to_check:
                # If the node reached via reference, keywords, or array items is the node itself, we have a circular
                # reference.
                # We also check if the path is for a parent to save on cycles
                if node_to_check == self or self.node_is_parent(node_to_check):
                    circular_references[self] = True
                    return True

            new_to_check: Set[SchemaNode] = set()
            for node_to_check in to_check:
                if node_to_check.links_to:
                    new_to_check.add(node_to_check.links_to)
                new_to_check = new_to_check.union(
                    set(n for n in node_to_check.keywords.values() if isinstance(n, SchemaNode))
                )
                new_to_check = new_to_check.union(set(node_to_check.array_items))
            to_check = new_to_check
            iteration_count += 1

        circular_references[self] = False
        return False

    def __eq__(self, other: object) -> bool:
        """For two schema nodes to be considered equals they must represent the same element in the same file"""
        if other is None:
            return False

        if not isinstance(other, SchemaNode):
            return NotImplemented

        return self.file == other.file and self.path_to_element == other.path_to_element

    def __hash__(self) -> int:
        return hash(self.file + self.flat_path)

    def __str__(self) -> str:
        return self.flat_path
