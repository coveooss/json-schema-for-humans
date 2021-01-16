import os
import tempfile

import pytest
from bs4 import BeautifulSoup

import tests.html_schema_doc_asserts
from json_schema_for_humans.generate import generate_from_file_object, GenerationConfiguration
from tests.test_utils import generate_case


def test_basic() -> None:
    """Test rendering a basic schema with title"""
    soup = generate_case("basic")

    tests.html_schema_doc_asserts.assert_basic_case(soup)


def test_multiple_types() -> None:
    """Test rendering a schema with type being an array."""
    soup = generate_case("multiple_types")

    tests.html_schema_doc_asserts.assert_types(
        soup, ["object", "string", "string or null", "integer or number", "integer, string, number or null"]
    )


def test_geo() -> None:
    """Test rendering a schema with numerical values that have restrictions"""
    soup = generate_case("geo")

    tests.html_schema_doc_asserts.assert_property_names(soup, ["latitude", "longitude"])
    tests.html_schema_doc_asserts.assert_types(soup, ["object", "number", "number"])
    tests.html_schema_doc_asserts.assert_numeric_restrictions(
        soup,
        [
            "Value must be greater or equal to -90 and lesser or equal to 90",
            "Value must be greater or equal to -180 and lesser or equal to 180",
        ],
    )
    tests.html_schema_doc_asserts.assert_required(soup, [True] * 2)


def test_references() -> None:
    """Test rendering a schema with references"""
    soup = generate_case("references")

    tests.html_schema_doc_asserts.assert_property_names(
        soup,
        [
            "a_gift",
            "anchor_with_slash",
            "propertyA",
            "anchor_no_slash",
            "anchor_nested_reference",
            "same_file_anchor_with_slash",
            "same_file_anchor_no_slash",
            "same_file_nested_reference",
            "other_file_anchor",
            "with_wrap",
            "other_file_dot_anchor",
            "other_file_dot_dot_anchor",
            "other_file_only",
            "not_a_string",
            "multi_hierarchy_reference",
            "propertyA",
        ],
    )
    tests.html_schema_doc_asserts.assert_descriptions(
        soup,
        [
            "Testing $ref",
            "A gift, or is it?",
            "Description for object_def/items/propertyA",
            "Description for array_def",
            "Description for string_def",
            "The delivery is a gift, no prices displayed",
            "The delivery is a gift, no prices displayed",
            "The delivery is a gift, no prices displayed",
            "Test schema with a not",
            "Contents of propertyA in final.json",
        ],
    )
    tests.html_schema_doc_asserts.assert_types(
        soup,
        [
            "object",  # root
            "string",  # a_gift
            "object",  # anchor_with_slash
            "string",  # anchor_with_slash -> propertyA
            "array of string",  # anchor_no_slash
            "string",  # anchor_no_slash items
            "string",  # anchor_nested_reference
            "string",  # same_file_anchor_with_slash
            "object",  # same_file_anchor_no_slash
            "string",  # same_file_nested_reference
            "object",  # other_file_anchor
            "boolean",  # other_file_anchor -> with_wrap
            "object",  # other_file_dot_anchor
            "object",  # other_file_dot_dot_anchor
            "object",  # other_file_only
            "string",  # not_a_string, not
            "object",  # multi_hierarchy_reference
            "string",  # multi_hierarchy_reference -> propertyA
        ],
    )


def test_references_url() -> None:
    """Test rendering a schema with references as URL"""

    soup = generate_case("references_url")

    tests.html_schema_doc_asserts.assert_property_names(soup, ["firstName"])
    tests.html_schema_doc_asserts.assert_descriptions(soup, ["Testing $ref with URL", "The person's first name."])
    tests.html_schema_doc_asserts.assert_types(soup, ["object", "string"])


def test_references_url_two_levels() -> None:
    """Test rendering a schema with references as URL"""

    soup = generate_case("references_url_two_levels")

    tests.html_schema_doc_asserts.assert_descriptions(soup, ["Testing $ref of a remote $ref"] + ["a filled string"] * 2)


def test_references_url_yaml() -> None:
    """Test rendering a schema with references as URL pointing to a YAML file"""

    soup = generate_case("references_url_yaml")

    tests.html_schema_doc_asserts.assert_property_names(soup, ["address", "street_address", "city", "state"])
    tests.html_schema_doc_asserts.assert_descriptions(soup, ["Testing $ref with URL with YAML destination"])
    tests.html_schema_doc_asserts.assert_types(soup, ["object", "object", "string", "string", "string"])


def test_additional_properties() -> None:
    """Test rendering a schema with additionalProperties: true, false, and a complex schema"""
    soup = generate_case("additional_properties")

    tests.html_schema_doc_asserts.assert_property_names(
        soup,
        [
            "subType1",
            "subProp1",
            "subType2",
            "subProp2",
            "Additional Properties",  # from subType2
            "Additional Properties",  # from top level of schema
            "propA",  # schema for top level additionalProperties
        ],
    )
    tests.html_schema_doc_asserts.assert_descriptions(
        soup,
        [
            "A sub type with additionalProperties false.",
            "A sub type with additionalProperties true.",
            "additionalProperties schema.",
        ],
    )

    explanation_nodes = soup.find_all(class_="additional-properties")
    assert [node.text for node in explanation_nodes] == [
        "Additional Properties of any type are allowed.",
        "Each additional property must conform to the following schema",
    ]

    # badge for the first sub type with additionalProperties: false
    badges = soup.find_all("span", class_=["no-additional"])
    assert len(badges) == 1
    badge = badges[0]
    assert badge.text == "No Additional Properties"


def test_top_level_array() -> None:
    """Test rendering a schema with an array instead of an object at the top level"""
    soup = generate_case("top_level_array")

    tests.html_schema_doc_asserts.assert_title(soup, "Array at top level")
    tests.html_schema_doc_asserts.assert_descriptions(soup, ["Sometimes there are no properties", "A string"])


def test_top_level_combining() -> None:
    """Test rendering a schema with a combining property at the top level"""
    soup = generate_case("top_level_combining")

    tests.html_schema_doc_asserts.assert_title(soup, "Combining at top level")
    tests.html_schema_doc_asserts.assert_descriptions(soup, ["For the combine"])
    tests.html_schema_doc_asserts.assert_types(soup, ["object"] * 4)


def test_array() -> None:
    """Test rendering a schema with arrays of elements having their own schema"""
    soup = generate_case("array")

    tests.html_schema_doc_asserts.assert_property_names(soup, ["fruits", "vegetables", "veggieName", "veggieLike"])
    tests.html_schema_doc_asserts.assert_descriptions(
        soup,
        [
            "A schema with an array",
            "The name of the vegetable.",
            "Do I like this vegetable?",
        ],
    )
    tests.html_schema_doc_asserts.assert_types(
        soup, ["object", "array of string", "string", "array", "object", "string", "boolean"]
    )
    tests.html_schema_doc_asserts.assert_required(soup, [False, False, True, True])


def test_array_advanced():
    """Test rendering a schema that uses minItems, maxItems, and uniqueItems for arrays"""
    soup = generate_case("array_advanced")

    tests.html_schema_doc_asserts.assert_descriptions(soup, ["A little food fun", "5 to 8 fruits that you like"])
    tests.html_schema_doc_asserts.assert_property_names(soup, ["fruits", "vegetables"])
    tests.html_schema_doc_asserts.assert_const(soup, ["eggplant"])
    tests.html_schema_doc_asserts.assert_required(soup, [False] * 2)


def test_with_definitions():
    """Test rendering a schema that uses the $ref keyword to refer to a definition attribute elsewhere in the schema"""
    soup = generate_case("with_definitions")

    tests.html_schema_doc_asserts.assert_property_names(
        soup,
        ["billing_address", "street_address", "city", "state", "shipping_address"],
    )
    tests.html_schema_doc_asserts.assert_types(soup, ["object", "object", "string", "string", "string", "object"])
    tests.html_schema_doc_asserts.assert_required(soup, [False, True, True, True, False])


def test_with_multiple_descriptions():
    """Test rendering a schema that uses multiple descriptions including with the $ref keyword"""
    soup = generate_case("with_descriptions")

    tests.html_schema_doc_asserts.assert_descriptions(
        soup,
        [
            "Exact address",
            "Exact address",
            "Delivery info depending on the delivery type",
            "The delivery is a gift, no prices displayed",
        ],
    )


def test_combining_one_of():
    """Test rendering of oneOf schema attribute in tabs"""
    soup = generate_case("combining_oneOf")

    tests.html_schema_doc_asserts.assert_one_of_options_names(soup, ["diskDevice", "diskUUID", "nfs", "tmpfs"])
    tests.html_schema_doc_asserts.assert_types(soup, ["object"] * 5)
    tests.html_schema_doc_asserts.assert_required(soup, [True])


def test_combining_not():
    """Test rendering of the not schema attribute"""
    soup = generate_case("combining_not")

    not_value = soup.find_all(class_="not-value")
    assert len(not_value) == 1

    assert not_value[0].text.lstrip().startswith("Must not be:")


def test_combining_any_of_option_names():
    soup = generate_case("anyOf_option_names")

    tests.html_schema_doc_asserts.assert_any_of_options_names(soup, ["diskDevice", "diskUUID", "Option 3", "tmpfs"])


def test_with_default() -> None:
    """Test rendering of default values"""
    soup = generate_case("with_default")

    tests.html_schema_doc_asserts.assert_default_values(soup, ['"Linux"', '["white", "blue"]', "2"])


def test_deprecated_in_description() -> None:
    """Test finding whether a property is deprecated from its description"""
    soup = generate_case("deprecated", GenerationConfiguration(deprecated_from_description=True))

    tests.html_schema_doc_asserts.assert_property_names(soup, ["deprecated1", "deprecated2", "not_deprecated"])
    tests.html_schema_doc_asserts.assert_deprecated(soup, [True, True, False])


def test_deprecated_not_in_description() -> None:
    """Test that the deprecated badge does not get added if the option to get deprecated from description is disabled"""
    soup = generate_case("deprecated", GenerationConfiguration(deprecated_from_description=False))

    tests.html_schema_doc_asserts.assert_deprecated(soup, [False] * 3)


def test_with_special_chars() -> None:
    soup = generate_case("with_special_chars", GenerationConfiguration(deprecated_from_description=False))

    tests.html_schema_doc_asserts.assert_property_names(soup, ["prénom", "nomDeFamille", "âge", "0 de quoi d'autre"])

    buttons = soup.find_all("button", attrs={"aria-controls": True})
    expected_targets = ["#pr_nom", "#nomDeFamille", "#a_ge", "#a0_de_quoi_d_autre"]
    for i, expected_target in enumerate(expected_targets):
        assert buttons[i].attrs["data-target"] == expected_target


def test_description_with_ref() -> None:
    """Test that having a description next to a $ref in an object uses that description and not the one from the
    referenced object
    """
    soup = generate_case("description_with_ref")

    tests.html_schema_doc_asserts.assert_descriptions(
        soup, ["We should see this", "inner description", "We should see this too"]
    )


def test_description_from_ref() -> None:
    """Test that having a description next to a $ref in an object uses that description and not the one from the
    referenced object
    """
    soup = generate_case("description_from_ref")

    tests.html_schema_doc_asserts.assert_descriptions(soup, ["a filled string"] * 2)


def test_description_with_ref_link_to_reused_ref() -> None:
    """Same as "test_description_with_ref", but do not allow reusing references."""
    soup = generate_case("description_with_ref", GenerationConfiguration(link_to_reused_ref=False))

    tests.html_schema_doc_asserts.assert_descriptions(
        soup, ["We should see this", "inner description", "We should see this too", "inner description"]
    )


def test_description_markdown_with_default_options() -> None:
    """Override default options """
    soup = generate_case("description_markdown", GenerationConfiguration())

    assert (
        str(soup.find("span", class_="description"))
        == '<span class="description"><p>DOC<br/> * List 1<br/> * List 2</p> </span>'
    )


def test_description_markdown_with_custom_options() -> None:
    """Same as "test_description_markdown_with_default_options" but with option to render list """
    soup = generate_case(
        "description_markdown",
        GenerationConfiguration(
            markdown_options={
                "cuddled-lists": True,
            }
        ),
    )

    assert (
        str(soup.find("span", class_="description"))
        == """<span class="description"><p>DOC </p> <ul> <li>List 1</li> <li>List 2</li> </ul> </span>"""
    )


def test_with_examples() -> None:
    soup = generate_case("with_examples")

    examples_label = soup.find_all("div", class_=["badge", "badge-secondary"])
    examples_label_text = [ex.text for ex in examples_label]
    assert examples_label_text == ["Examples:", "Example:", "Example:", "Example:"]

    examples_content = soup.find_all("div", class_="examples")
    examples_content_text = [ex.findChildren()[0].text for ex in examples_content]
    assert examples_content_text == [
        '"Guido"\n',
        '"BDFL"\n',
        '"Van Rossum"\n',
        "64\n",
        """{
    "birthplace": "Haarlem, Netherlands",
    "favorite_emoji": "🐍",
    "motto": "Beautiful is better than ugly.\\\\nExplicit is better than implicit.\\\\nSimple is better than complex.\\\\nComplex is better than complicated.\\\\nFlat is better than nested.\\\\nSparse is better than dense.\\\\nReadability counts.\\\\nSpecial cases aren't special enough to break the rules.\\\\nAlthough practicality beats purity.\\\\nErrors should never pass silently.\\\\nUnless explicitly silenced.\\\\nIn the face of ambiguity, refuse the temptation to guess.\\\\nThere should be one-- and preferably only one --obvious way to do it.\\\\nAlthough that way may not be obvious at first unless you're Dutch.\\\\nNow is better than never.\\\\nAlthough never is often better than *right* now.\\\\nIf the implementation is hard to explain, it's a bad idea.\\\\nIf the implementation is easy to explain, it may be a good idea.\\\\nNamespaces are one honking great idea -- let\'s do more of those!"
}\n""",
    ]


def test_pattern_properties() -> None:
    soup = generate_case("pattern_properties")

    pattern_label = soup.find_all("span", class_=["badge-info"])
    pattern_label_text = [ex.text for ex in pattern_label]
    assert pattern_label_text == ["Pattern Property"]

    pattern_content = soup.find_all("span", class_="pattern-value")
    pattern_content_text = [ex.findChildren()[0].text for ex in pattern_content]
    assert pattern_content_text == ["$[a-c][0-9]^"]

    tests.html_schema_doc_asserts.assert_property_names(
        soup, ["firstName", "lastName", "paperSize", "rating", "review"]
    )

    tests.html_schema_doc_asserts.assert_descriptions(
        soup,
        [
            "The person's first name.",
            "The person's last name.",
            "Review of a paper size.",
            "Numerical rating for paper size.",
            "Narrative review of the paper size.",
        ],
    )


def test_pattern_properties_html_id() -> None:
    """Test the HTML IDs generated for patterns under patternProperties"""
    soup = generate_case("pattern_properties_html_id")

    pattern_label = soup.find_all("span", class_=["badge-info"])
    pattern_label_text = [ex.text for ex in pattern_label]
    assert pattern_label_text == ["Pattern Property"] * 4

    pattern_content = soup.find_all("span", class_="pattern-value")
    pattern_content_text = [ex.findChildren()[0].text for ex in pattern_content]
    assert pattern_content_text == [".$", ".*", "..", "^."]

    tests.html_schema_doc_asserts.assert_property_names(
        soup, ["not_a_pattern", "Title 4", "Title 1", "Title 2", "Title 3"]
    )

    tests.html_schema_doc_asserts.assert_descriptions(
        soup,
        ["Description 4", "Description 1", "Description 2", "Description 3"],
    )

    property_divs = soup.find_all("div", class_="property-definition-div")
    property_divs_id = [div.attrs["id"] for div in property_divs]
    assert property_divs_id == ["not_a_pattern", "not_a_pattern_pattern1", "pattern1", "pattern2", "pattern3"]


def test_conditional_subschema() -> None:
    soup = generate_case("conditional_subschema")

    tests.html_schema_doc_asserts.assert_types(
        soup, ["object", "object", "const", "object", "object", "object", "object", "string", "enum (of string)"]
    )


def test_html_in_patterns() -> None:
    soup = generate_case("html_in_patterns")

    code_blocks = soup.find_all("code")
    assert list(block.text for block in code_blocks) == [
        "^(<<variable:([-+/*0-9A-Za-z_]+)>>|<<auto>>)$",
        "$[a-c][0-9]^<a>",
    ]

    tests.html_schema_doc_asserts.assert_property_names(soup, ["$[a-c][0-9]^<a>"])


def test_yaml() -> None:
    """Test loading the schema from a YAML file. The schema is the same as the case "with_definitions"."""
    with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "cases", f"yaml.yaml"))) as schema_fp:
            generate_from_file_object(schema_fp, temp_file, True, False, False, True)

        temp_file.seek(0)
        soup = BeautifulSoup(temp_file.read(), "html.parser")

    # Order of properties is only preserved in Python 3.7+
    tests.html_schema_doc_asserts.assert_property_names(
        soup,
        ["billing_address", "street_address", "city", "state", "shipping_address"],
    )
    tests.html_schema_doc_asserts.assert_types(soup, ["object", "object", "string", "string", "string", "object"])
    tests.html_schema_doc_asserts.assert_required(soup, [False, True, True, True, False])


def test_single_element_allOf() -> None:
    """Test loading schema that has a single-element allOf property"""
    soup = generate_case("single_element_allOf")

    tests.html_schema_doc_asserts.assert_title(soup, "Schema containing a single-element allOf")
    tests.html_schema_doc_asserts.assert_descriptions(
        soup, ["Schema containing a single-element allOf", "My string definition"]
    )


def test_json_with_tabs() -> None:
    """Test loading the schema when tabs are present rather than spaces. Regression test for #45"""
    temp_schema_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json")
    created_filename = temp_schema_file.name
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "cases", f"basic.json"))) as schema_fp:
        for line in schema_fp:
            temp_schema_file.write(line.replace("  ", "\t"))
    with tempfile.NamedTemporaryFile(mode="w+") as temp_html_file:
        temp_schema_file.seek(0)
        generate_from_file_object(temp_schema_file, temp_html_file, True, False, False, True)
        temp_schema_file.close()
        os.remove(created_filename)
        temp_html_file.seek(0)
        soup = BeautifulSoup(temp_html_file.read(), "html.parser")
        tests.html_schema_doc_asserts.assert_basic_case(soup)


def test_schema_with_keywords_as_properties() -> None:
    """Test rendering a schema in which properties are named the same as JSON schema keywords"""
    soup = generate_case("with_keywords")
    keywords = ["default", "examples", "if", "then", "else", "anyOf", "allOf", "not", "properties", "patternProperties"]
    tests.html_schema_doc_asserts.assert_property_names(soup, keywords)
    tests.html_schema_doc_asserts.assert_descriptions(soup, keywords)


def test_ref_merge() -> None:
    """Test case where a schema has elements next to $ref"""
    soup = generate_case("ref_merge")

    tests.html_schema_doc_asserts.assert_descriptions(soup, ["This is the description from the definition"])
    tests.html_schema_doc_asserts.assert_types(soup, ["object", "enum (of string)", "object", "string", "string"])
    tests.html_schema_doc_asserts.assert_property_names(soup, ["aProperty", "aDictPropertyARequired", "a", "b"])
    tests.html_schema_doc_asserts.assert_default_values(soup, ['"Default from property"', '{"a": "a", "b": "b"}'])
    tests.html_schema_doc_asserts.assert_enum_values(soup, [['"value1"', '"value2"']])
    # a and b are required from the definition
    tests.html_schema_doc_asserts.assert_required(soup, [False, False, True, True])


def test_circular_reference() -> None:
    """Test that generating a schema that has circular references does not crash"""
    soup = generate_case("circular")

    tests.html_schema_doc_asserts.assert_types(soup, ["object", "object", "string"])
    tests.html_schema_doc_asserts.assert_property_names(soup, ["person", "a1"])
    tests.html_schema_doc_asserts.assert_descriptions(soup, ["Description from b"])
    tests.html_schema_doc_asserts.assert_default_values(soup, ['"Default from c"'])


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_defaults_with_merge(link_to_reused_ref: bool) -> None:
    """Test default values being displayed correctly when they come from a common ref"""
    soup = generate_case("defaults", GenerationConfiguration(link_to_reused_ref=link_to_reused_ref))

    tests.html_schema_doc_asserts.assert_types(soup, ["object", "object", "object"])
    tests.html_schema_doc_asserts.assert_descriptions(soup, ["Description of a", "A common description"])
    tests.html_schema_doc_asserts.assert_property_names(soup, ["a", "b"])
    tests.html_schema_doc_asserts.assert_default_values(soup, ['"Default from a"', '"Default from b"'])


@pytest.mark.parametrize("collapse", [True, False])
def test_long_description(collapse: bool) -> None:
    soup = generate_case("long_description", GenerationConfiguration(collapse_long_descriptions=collapse))

    read_more = soup.find("a", href="#collapseDescription_it_s_hard_to_explain")

    if collapse:
        assert read_more
    else:
        assert not read_more


# TODO: test for uniqueItems
# TODO: test for contains
