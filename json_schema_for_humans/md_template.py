from typing import Dict, List, Optional, Union
from urllib.parse import quote, quote_plus

import jinja2

from json_schema_for_humans import const, jinja_filters
from json_schema_for_humans.schema.schema_node import SchemaNode
from json_schema_for_humans.templating_utils import schema_keyword_to_int


def get_numeric_maximum_restriction(schema_node: SchemaNode, default: str = "N/A") -> str:
    """Filter. Get the text to display about maximum restriction on a numeric type(integer or number)"""
    maximum = schema_keyword_to_int(schema_node, const.MAXIMUM)
    exclusive_maximum = schema_keyword_to_int(schema_node, const.EXCLUSIVE_MAXIMUM)

    # Fix maximum and exclusive_maximum both there
    if maximum is not None and exclusive_maximum is not None:
        if maximum > exclusive_maximum:
            exclusive_maximum = None
        else:
            maximum = None

    maximum_fragment = default
    if maximum is not None:
        maximum_fragment = f"&le; {maximum}"
    if exclusive_maximum is not None:
        maximum_fragment = f"&lt; {exclusive_maximum}"

    return maximum_fragment


def escape_for_table(example_text: Optional[str]) -> str:
    """Filter. escape characters('|', '`') in string to be inserted into Markdown table"""
    if example_text is None:
        return ""
    return example_text.translate(str.maketrans({"|": "\\|", "`": "\\`", "\n": "<br />"}))  # type:ignore[arg-type]


def get_numeric_minimum_restriction(schema_node: SchemaNode, default: str = "N/A") -> str:
    """Filter. Get the text to display about minimum restriction on a numeric type (integer or number)"""
    minimum = schema_keyword_to_int(schema_node, const.MINIMUM)
    exclusive_minimum = schema_keyword_to_int(schema_node, const.EXCLUSIVE_MINIMUM)

    # Fix minimum and exclusive_minimum both there
    if minimum is not None and exclusive_minimum is not None:
        if minimum <= exclusive_minimum:
            exclusive_minimum = None
        else:
            minimum = None

    minimum_fragment = default
    if minimum is not None:
        minimum_fragment = f"&ge; {minimum}"
    if exclusive_minimum is not None:
        minimum_fragment = f"&gt; {exclusive_minimum}"

    return minimum_fragment


def generate_table(table: List[List[str]]) -> str:
    """
    Pretty print markdown table using list of rows.
    Assuming first row is header line.
    Ending with empty line for rendering bottom border.
    Each column is str padded to max size string in the column.
    """
    if len(table) == 0:
        return ""

    # compute max length of each column
    max_cell_length: Dict = {}
    for idx_row, row in enumerate(table):
        for idx_col, cell in enumerate(row):
            max_cell_length[idx_col] = max(max_cell_length.get(idx_col, 0), len(cell))

    # generate md table
    output = ""
    for idx_row, row in enumerate(table):
        for idx_col, cell in enumerate(row):
            output += "| " + cell.ljust(max_cell_length[idx_col], " ") + " "
        output += "|\n"
        # add header line
        if idx_row == 0:
            for idx_col, cell in enumerate(row):
                output += "| " + "".ljust(max_cell_length[idx_col], "-") + " "
            output += "|\n"

    return output


def restrictions_table(schema: SchemaNode) -> List[List[str]]:
    """
    String or numeric restrictions tables
    - min/max length
    - regexp pattern + link to regexp101
    - multipleOf
    - minimum/maximum
    ready to be rendered by generate_table filter
    """
    restrictions = []
    if schema.kw_min_length:
        restrictions.append(["**Min length**", str(schema.kw_min_length.literal)])
    if schema.kw_max_length:
        restrictions.append(["**Max length**", str(schema.kw_max_length.literal)])
    if schema.kw_pattern and schema.kw_pattern.literal_str:
        pattern_code = schema.kw_pattern.literal_str.replace("|", "\\|")
        pattern_url = quote_plus(schema.kw_pattern.literal_str)
        example_url = ""
        if len(schema.examples) > 0:
            example_url = "&testString=" + quote_plus(schema.examples[0])
        restrictions.append(
            [
                "**Must match regular expression**",
                f"```{pattern_code}``` [Test](https://regex101.com/?regex={pattern_url}{example_url})",
            ]
        )
    if schema.kw_multiple_of and schema.kw_multiple_of.literal_to_str:
        restrictions.append(["**Multiple of**", schema.kw_multiple_of.literal_to_str])
    if schema.kw_minimum or schema.kw_exclusive_minimum:
        restrictions.append(["**Minimum**", str(get_numeric_minimum_restriction(schema))])
    if schema.kw_maximum or schema.kw_exclusive_maximum:
        restrictions.append(["**Maximum**", str(get_numeric_maximum_restriction(schema))])

    if len(restrictions) > 0:
        # add header
        restrictions.insert(0, ["Restrictions", " "])

    return restrictions


def array_items(schema: SchemaNode, title: str) -> List[List[str]]:
    """
    List of array items
    ready to be rendered by generate_table filter
    """
    if not schema.array_items:
        return []
    items = [[title]]
    for i, item in enumerate(schema.array_items):
        item_label = item.name_for_breadcrumbs or f"{title} {i}"
        item_html_id = item.html_id
        items.append([f"[{item_label}](#{item_html_id})"])

    return items


def first_line_fixed(example_text: str) -> str:
    """first_line but replace ` with ' to avoid unbalanced `s in markdown"""
    return jinja_filters.first_line(example_text).translate(str.maketrans({"`": "'"}))  # type:ignore[arg-type]


def array_items_restrictions(schema: SchemaNode) -> List[List[str]]:
    """
    Tuple validation restrictions
    ready to be rendered by generate_table filter
    """
    if not schema.array_items_def and not schema.tuple_validation_items:
        return []

    items_restriction_rules = (
        [schema.array_items_def] if schema.array_items_def else []
    ) + schema.tuple_validation_items
    items_restrictions = [["Each item of this array must be", "Description"]]
    for i, item in enumerate(items_restriction_rules):
        item_label = item.name_for_breadcrumbs or f"Array Item {i}"
        item_html_id = item.html_id
        items_restrictions.append(
            [
                f"[{item_label}](#{item_html_id})",
                escape_for_table(first_line_fixed(item.description or "-")),
            ]
        )

    return items_restrictions


class MarkdownTemplate(object):
    def __init__(self, config):
        self.headings = {}
        self.auto_generated_heading = 0
        self.toc = {}
        self.config = config

        self.should_conform_badge = self.badge("Should-conform", "blue")
        if self.config.md_badge_as_image:
            self.badge_not_allowed = self.badge("Not allowed", "red")
            self.badge_allowed = self.badge("Any type", "green", "allowed")
            self.deprecated_badge = self.badge("Deprecated", "red")
            self.required_badge = self.badge("Required", "blue")
            self.optional_badge = self.badge("Optional", "yellow")
        else:
            self.badge_not_allowed = "Not allowed"
            self.badge_allowed = "Any type allowed"
            self.deprecated_badge = "Deprecated"
            self.required_badge = ""
            self.optional_badge = ""

    def register_jinja(self, env: jinja2.Environment):
        env.filters["md_get_numeric_minimum_restriction"] = get_numeric_minimum_restriction
        env.filters["md_get_numeric_maximum_restriction"] = get_numeric_maximum_restriction
        env.filters["md_escape_for_table"] = escape_for_table
        env.filters["md_heading"] = self.heading
        env.filters["md_properties_table"] = self.properties_table
        env.filters["md_type_info_table"] = self.type_info_table
        env.filters["md_array_restrictions"] = self.array_restrictions
        env.filters["md_array_items_restrictions"] = array_items_restrictions
        env.filters["md_array_items"] = array_items
        env.filters["md_restrictions_table"] = restrictions_table
        env.filters["md_generate_table"] = generate_table

        env.globals["required_badge"] = self.required_badge
        env.globals["optional_badge"] = self.optional_badge
        env.globals["md_get_toc"] = self.get_toc

    def heading(self, title: str, depth: int, html_id: Union[bool, str] = False, nested: bool = False) -> str:
        """
        Filter. display heading menu, heading number automatically calculated
        from previous heading and depth provided
        """
        if depth == 0:
            # If we process multiple files, this needs to be reset manually
            # because there is only one instance of this class
            self.toc = {}
            self.auto_generated_heading = 0

        if not html_id:
            self.auto_generated_heading = self.auto_generated_heading + 1
            html_id = f"autogenerated_heading_{self.auto_generated_heading}"
        if not (title and title.strip()):
            title = "Auto generated title"
        else:
            title = title.strip()

        # reset heading depth greater than current depth
        for curDepth in range(
            depth + 1, max(int(heading) for heading in self.headings) + 1 if self.headings else depth + 1
        ):
            self.headings.pop(curDepth, None)

        # compute heading, for each depth get last level, and increment level of asked depth
        heading_numbers = ""
        for curDepth in range(0, depth + 1):
            if curDepth in self.headings:
                if curDepth == depth:
                    self.headings[curDepth] = self.headings[curDepth] + 1
            else:
                self.headings[curDepth] = 1
            if curDepth != 0:
                heading_numbers += f"{self.headings[curDepth]}."

        # markdown menu depth
        menu = "#" * min((depth + 1), 6)
        if nested:
            menu = "<strong>"

        # generate markdown title with anchor (except if depth 0)
        if depth == 0:
            menu += f" {title}"
        else:
            if self.config.template_md_options.get("show_heading_numbers"):
                menu += f' <a name="{html_id}"></a>{heading_numbers} {title}'
            else:
                menu += f' <a name="{html_id}"></a>{title}'

        # store current heading in toc
        toc_menu = f"[{title}](#{html_id})"
        if self.config.template_md_options.get("show_heading_numbers"):
            toc_menu = f"[{heading_numbers} {title}](#{html_id})"
        self.toc[heading_numbers] = {"depth": depth, "menu": toc_menu}

        if nested:
            menu += "</strong>"
        return menu

    def get_toc(self) -> str:
        """
        generate Table Of Content from the heading that has been generated
        """
        if not self.config.show_toc:
            return ""

        toc_str = ""

        second_heading_depth = 0
        for i, heading in enumerate(self.toc.values()):
            # Ignore first heading
            if i == 0:
                continue
            if i == 1:
                second_heading_depth = heading["depth"]

            # Ensure we have no space at first level for TOC to be recognized
            indent = "  " * (heading["depth"] - second_heading_depth)
            toc_str += indent + "- " + heading["menu"] + "\n"

        return toc_str

    @staticmethod
    def format_link(title: str, link: str, tooltip: str = "") -> str:
        """Format a Markdown link"""
        return f"[{title}](#{link} {tooltip})"

    def badge(self, name: str, color: str, value: str = "") -> str:
        """
        Badge as markdown image link
        """
        if value:
            text_badge = f"{name}: {value}"
        else:
            text_badge = name

        value_str = ""
        if value:
            value_str = "-" + quote(value)
        name = quote(name)
        color = quote(color)
        return f"![{text_badge}](https://img.shields.io/badge/{name}{value_str}-{color})"

    def properties_table(self, schema: SchemaNode) -> List[List]:
        """
        Generate list of properties ready to be rendered by generate_table filter
        """
        properties = []
        for sub_property in schema.iterate_properties:
            line: List[str] = []
            for field in self.config.template_md_options.get("properties_table_columns"):
                if field == "Property":
                    # property name
                    property_name = "+ " if sub_property.is_required_property else "- "
                    property_name += self.format_link(
                        escape_for_table(sub_property.property_name), sub_property.html_id
                    )
                    line.append(property_name)
                elif field == "Pattern":
                    # pattern
                    line.append("Yes" if sub_property.is_pattern_property else "No")
                elif field == "Type":
                    # type
                    line.append(
                        "Combination"
                        if jinja_filters.is_combining(sub_property)
                        else escape_for_table(sub_property.type_name)
                    )
                elif field == "Deprecated":
                    # Deprecated
                    line.append(self.deprecated_badge if jinja_filters.deprecated(self.config, sub_property) else "No")
                elif field == "Definition":
                    # Link
                    if sub_property.should_be_a_link(self.config):
                        assert sub_property.links_to
                        line.append(
                            "Same as "
                            + self.format_link(sub_property.links_to.link_name, sub_property.links_to.html_id)
                        )
                    elif sub_property.refers_to:
                        line.append("In " + sub_property.ref_path)
                    else:
                        line.append("-")
                elif field == "Title/Description":
                    # title or description
                    description = sub_property.description or "-"
                    if sub_property.title:
                        description = sub_property.title
                    line.append(escape_for_table(description))
                else:
                    raise ValueError(f"Unknown field {field} for properties table")

            properties.append(line)

        if properties:
            # add header
            headers = self.config.template_md_options.get("properties_table_columns")
            properties.insert(0, headers)

        return properties

    def type_info_table(self, schema: SchemaNode) -> List[List]:
        """
        Schema type info table :
        - type,
        - additional properties,
        - default value,
        - definitions links
        ready to be rendered by generate_table filter
        """
        type_info = []

        schema_type = schema.type_name
        default_value = schema.default_value
        schema_format = schema.format

        merged_schema = schema if not schema.refers_to else schema.refers_to_merged
        assert merged_schema

        type_info.append(["", ""])
        type_info.append(
            ["**Type**", "`combining`" if jinja_filters.is_combining(merged_schema) else f"`{schema_type}`"]
        )
        if not self.config.md_badge_as_image:
            type_info.append(["**Required**", "Yes" if schema.is_required_property else "No"])
        if jinja_filters.deprecated(self.config, merged_schema):
            type_info.append(["**Deprecated**"])
            if self.config.md_badge_as_image:
                type_info.append(self.deprecated_badge)

        if schema_format:
            type_info.append(["**Format**", f"`{schema_format}`"])
        if schema_type == const.TYPE_OBJECT:
            type_info.append(["**Additional properties**", self.additional_properties(merged_schema)])
        if default_value:
            type_info.append(["**Default**", f"`{default_value}`"])
        if schema.should_be_a_link(self.config):
            assert schema.links_to
            schema_link_name = schema.links_to.link_name
            html_id = schema.links_to.html_id
            type_info.append(["**Same definition as**", f"[{ schema_link_name }](#{ html_id })"])
        elif schema.refers_to:
            type_info.append(["**Defined in**", schema.ref_path])

        return type_info

    def additional_properties(self, schema: SchemaNode) -> str:
        """additional properties badge generation"""
        additional_properties = ""

        for sub_property in schema.iterate_properties:
            if sub_property.is_additional_properties:
                if sub_property.is_additional_properties_schema:
                    html_id = sub_property.html_id
                    if self.config.md_badge_as_image:
                        additional_properties = f"[{self.should_conform_badge}](#{html_id})"
                    else:
                        additional_properties = f"[Each additional property must conform to the schema](#{html_id})"
                    break
                else:
                    additional_properties = self.badge_allowed
                    break

        if not additional_properties:
            if schema.explicit_no_additional_properties:
                additional_properties = self.badge_not_allowed
            else:
                additional_properties = self.badge_allowed

        return additional_properties

    def array_restrictions(self, schema: SchemaNode) -> List[List[str]]:
        """
        array restrictions: min/max items, items unicity, additional items, Tuple validation
        ready to be rendered by generate_table filter
        """

        if not self.config.template_md_options.get("show_array_restrictions"):
            return []

        return [
            ["", "Array restrictions"],
            ["**Min items**", str(schema.kw_min_items.literal) if schema.kw_min_items else "N/A"],
            ["**Max items**", str(schema.kw_max_items.literal) if schema.kw_max_items else "N/A"],
            [
                "**Items unicity**",
                "True" if schema.kw_unique_items and schema.kw_unique_items.literal is True else "False",
            ],
            [
                "**Additional items**",
                "True" if schema.array_additional_items else "False",
            ],
            [
                "**Tuple validation**",
                (
                    "See below"
                    if schema.array_items_def
                    or schema.tuple_validation_items
                    or (schema.kw_contains and schema.kw_contains.literal != {})
                    else "N/A"
                ),
            ],
        ]
