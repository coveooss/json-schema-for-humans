from typing import Dict, List, Union
from urllib.parse import quote_plus

import jinja2

from json_schema_for_humans import const, jinja_filters
from json_schema_for_humans.schema.schema_node import SchemaNode


def get_numeric_maximum_restriction(schema_node: SchemaNode, default: str = "N/A") -> str:
    """Filter. Get the text to display about maximum restriction on a numeric type(integer or number)"""
    maximum = schema_node.keywords.get(const.MAXIMUM)
    if maximum:
        maximum = maximum.literal
    exclusive_maximum = schema_node.keywords.get(const.EXCLUSIVE_MAXIMUM)
    if exclusive_maximum:
        exclusive_maximum = exclusive_maximum.literal

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


def escape_for_table(example_text: str) -> str:
    """Filter. escape characters('|', '`') in string to be inserted into markdown table"""
    return example_text.translate(str.maketrans({"|": "\\|", "`": "\\`"}))


def get_numeric_minimum_restriction(schema_node: SchemaNode, default: str = "N/A") -> str:
    """Filter. Get the text to display about minimum restriction on a numeric type (integer or number)"""
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

    # add last empty row
    for cell in max_cell_length.values():
        output += "| " + "".ljust(cell, " ") + " "
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
    if schema.kw_pattern:
        pattern_code = schema.kw_pattern.literal.replace("|", "\\|")
        pattern_url = quote_plus(schema.kw_pattern.literal)
        example_url = ""
        if len(schema.examples) > 0:
            example_url = "&testString=" + quote_plus(schema.examples[0])
        restrictions.append(
            [
                "**Must match regular expression**",
                f"```{pattern_code}``` [Test](https://regex101.com/?regex={pattern_url}{example_url})",
            ]
        )
    if schema.keywords.get("multipleOf"):
        restrictions.append(["**Multiple of**", str(schema.keywords.get("multipleOf").literal)])
    if schema.keywords.get("minimum") or schema.keywords.get("exclusiveMinimum"):
        restrictions.append(["**Minimum**", str(get_numeric_minimum_restriction(schema))])
    if schema.keywords.get("maximum") or schema.keywords.get("exclusiveMaximum"):
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


def first_line_fixed(example_text: str, max_length: int = 0) -> str:
    """first_line truncated but replace ` with ' to avoid to have only one ` to avoid issues with jekyll"""
    return jinja_filters.first_line(example_text, max_length).translate(str.maketrans({"`": "'"}))


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
                escape_for_table(first_line_fixed(item.description or "-", const.LINE_WIDTH)),
            ]
        )

    return items_restrictions


class MarkdownTemplate(object):
    def __init__(self, config):
        self.headings = {}
        self.auto_generated_heading = 0
        self.toc = {}
        self.config = config

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
        env.filters["md_first_line"] = first_line_fixed

        env.globals["md_badge"] = self.badge
        env.globals["md_get_toc"] = self.get_toc

    def heading(self, title: str, depth: int, html_id: Union[bool, str] = False, nested: bool = False) -> str:
        """
        Filter. display heading menu, heading number automatically calculated
        from previous heading and depth provided
        """
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
        menu = "#" * min((depth + 1), 5)
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

    def badge(self, name: str, color: str, value: str = "", show_text: bool = False) -> str:
        """
        Badge as markdown image link if badge_as_image option set otherwise Badge as text
        """
        if self.config.template_md_options.get("badge_as_image") and not show_text:
            value_str = ""
            if value and len(value) > 0:
                value_str = "-" + quote_plus(value)
            name = quote_plus(name)
            color = quote_plus(color)
            return f"![badge](https://img.shields.io/badge/{name}{value_str}-{color})"
        else:
            if value and len(value) > 0:
                return f"[{name}: {value}]"
            return f"[{name}]"

    def properties_table(self, schema: SchemaNode) -> List[List]:
        """
        Generate list of properties ready to be rendered by generate_table filter
        """
        properties = []
        for sub_property in schema.iterate_properties:
            line = []
            # property name
            property_name = "+ " if sub_property.is_required_property else "- "
            property_name += self.format_link(escape_for_table(sub_property.property_name), sub_property.html_id)
            line.append(property_name)
            # pattern
            line.append("Yes" if sub_property.is_pattern_property else "No")
            # type
            line.append(
                "Combination" if jinja_filters.is_combining(sub_property) else escape_for_table(sub_property.type_name)
            )
            # Deprecated
            line.append(
                self.badge("Deprecated", "red") if jinja_filters.deprecated(self.config, sub_property) else "No"
            )
            # Link
            if sub_property.should_be_a_link(self.config):
                line.append(
                    "Same as " + self.format_link(sub_property.links_to.link_name, sub_property.links_to.html_id)
                )
            elif sub_property.refers_to:
                line.append("In " + sub_property.ref_path)
            else:
                line.append("-")

            # title or description
            description = sub_property.description or "-"
            if sub_property.title:
                description = sub_property.title

            line.append(escape_for_table(first_line_fixed(description, const.LINE_WIDTH)))

            properties.append(line)

        if properties:
            # add header
            properties.insert(0, ["Property", "Pattern", "Type", "Deprecated", "Definition", "Title/Description"])

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
        type_info.append(["Type", "`combining`" if jinja_filters.is_combining(schema) else f"`{schema_type}`"])
        if jinja_filters.deprecated(self.config, schema):
            type_info.append(["**Deprecated**", self.badge("Deprecated", "red")])

        type_info.append(["**Additional properties**", self.additional_properties(schema)])
        if schema.default_value:
            type_info.append(["**Default**", f"`{default_value}`"])
        if schema.should_be_a_link(self.config):
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
                    should_conform_badge = self.badge("Should-conform", "blue")
                    additional_properties = f'[{should_conform_badge}](#{html_id} "Each additional property must conform to the following schema")'
                    break
                else:
                    badge_any_type = self.badge("Any type", "green", "allowed")
                    additional_properties = f'[{badge_any_type}](# "Additional Properties of any type are allowed.")'
                    break

        if len(additional_properties) == 0:
            if schema.explicit_no_additional_properties:
                badge_not_allowed = self.badge("Not allowed", "red")
                additional_properties = f'[{badge_not_allowed}](# "Additional Properties not allowed.")'
            else:
                badge_allowed = self.badge("Any type", "green", "allowed")
                additional_properties = f'[{badge_allowed}](# "Additional Properties of any type are allowed.")'

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
                "True" if schema.kw_additional_items and schema.kw_additional_items.literal is True else "False",
            ],
            [
                "**Tuple validation**",
                "See below"
                if schema.array_items_def
                or schema.tuple_validation_items
                or (schema.kw_contains and schema.kw_contains.literal != {})
                else "N/A",
            ],
        ]
