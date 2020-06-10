import os
import tempfile
from typing import List

import pytest
from bs4 import BeautifulSoup

from json_schema_for_humans.generate import generate_from_file_object, generate_from_schema
from tests.test_utils import _get_test_case_path


def _generate_case(
    case_name: str, find_deprecated: bool = False, find_default: bool = False, link_to_reused_ref: bool = True
) -> BeautifulSoup:
    """Get the BeautifulSoup object for a test case"""
    return BeautifulSoup(
        generate_from_schema(
            _get_test_case_path(case_name),
            None,
            False,
            find_deprecated,
            find_default,
            True,
            link_to_reused_ref=link_to_reused_ref,
        ),
        "html.parser",
    )


def _assert_soup_results_text(soup: BeautifulSoup, class_name: str, texts: List[str]) -> None:
    """Assert that all the HTML elements with the provided class found in the schema has the supplied text

    There must be exactly as many elements as the length of the supplied values and they must be in the same order
    """
    elements = soup.find_all(class_=class_name)

    assert len(elements) == len(texts)

    for i, element in enumerate(elements):
        assert element.text.strip() == texts[i]


def _assert_property_names(soup: BeautifulSoup, property_names: List[str]) -> None:
    _assert_soup_results_text(soup, "property-name", property_names)


def _assert_title(soup: BeautifulSoup, title: str) -> None:
    """Assert the result file contains the provided title"""
    assert soup.head.title.string == title
    assert soup.body.h1.string == title


def _assert_descriptions(soup: BeautifulSoup, descriptions: List[str]) -> None:
    """Assert the result file contains exactly the provided descriptions in the same order"""
    _assert_soup_results_text(soup, "description", descriptions)


def _assert_types(soup: BeautifulSoup, type_names: List[str]) -> None:
    _assert_soup_results_text(soup, "value-type", [f"Type: {type_name}" for type_name in type_names])


def _assert_const(soup: BeautifulSoup, const_values: List[str]) -> None:
    _assert_soup_results_text(soup, "const-value", [f'Specific value: "{const_value}"' for const_value in const_values])


def _assert_numeric_restrictions(soup: BeautifulSoup, restrictions: List[str]) -> None:
    _assert_soup_results_text(soup, "numeric-restriction", restrictions)


def _assert_one_of_options(soup: BeautifulSoup, nb_options: int) -> None:
    _assert_soup_results_text(soup, "oneOf-option", [f"Option {str(i + 1)}" for i in range(nb_options)])


def _assert_default_values(soup: BeautifulSoup, default_values: List[str]) -> None:
    _assert_soup_results_text(soup, "default-value", [f"Default: {default_value}" for default_value in default_values])


def _assert_badges(soup: BeautifulSoup, badge_class_name: str, expected_values: List[bool]) -> None:
    """Assert that the badge with the given class name is either present or not for all properties"""
    property_cards = soup.find_all(class_="property-name-button")
    assert len(property_cards) == len(expected_values)

    for i, property_card in enumerate(property_cards):
        assert (property_card.find(class_=f"{badge_class_name}-property") is not None) == expected_values[i]


def _assert_deprecated(soup: BeautifulSoup, is_deprecated_properties: List[bool]) -> None:
    _assert_badges(soup, "deprecated", is_deprecated_properties)


def _assert_required(soup: BeautifulSoup, is_required_properties: List[bool]) -> None:
    _assert_badges(soup, "required", is_required_properties)


def _assert_basic_case(soup: BeautifulSoup) -> None:
    """Assert the rendered result of the basic test case"""
    _assert_property_names(soup, ["firstName", "lastName", "age"])
    _assert_descriptions(
        soup,
        [
            "The person's first name.",
            "The person's last name.",
            "Age in years which must be equal to or greater than zero.",
        ],
    )
    _assert_title(soup, "Person")
    _assert_numeric_restrictions(soup, ["Value must be greater or equal to 0"])
    _assert_required(soup, [False] * 3)


def test_basic() -> None:
    """Test rendering a basic schema with title"""
    soup = _generate_case("basic")

    _assert_basic_case(soup)


def test_multiple_types() -> None:
    """Test rendering a schema with type being an array."""
    soup = _generate_case("multiple_types")

    _assert_types(soup, ["object", "string", "string or null", "integer or number", "integer, string, number or null"])


def test_geo() -> None:
    """Test rendering a schema with numerical values that have restrictions"""
    soup = _generate_case("geo")

    _assert_property_names(soup, ["latitude", "longitude"])
    _assert_types(soup, ["object", "number", "number"])
    _assert_numeric_restrictions(
        soup,
        [
            "Value must be greater or equal to -90 and lesser or equal to 90",
            "Value must be greater or equal to -180 and lesser or equal to 180",
        ],
    )
    _assert_required(soup, [True] * 2)


def test_references() -> None:
    """Test rendering a schema with references"""
    soup = _generate_case("references")

    _assert_property_names(
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
    _assert_descriptions(
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


def test_top_level_array() -> None:
    """Test rendering a schema with an array instead of an object at the top level"""
    soup = _generate_case("top_level_array")

    _assert_title(soup, "Array at top level")
    _assert_descriptions(soup, ["Sometimes there are no properties", "A string"])


def test_top_level_combining() -> None:
    """Test rendering a schema with a combining property at the top level"""
    soup = _generate_case("top_level_combining")

    _assert_title(soup, "Combining at top level")
    _assert_descriptions(soup, ["For the combine"])
    _assert_types(soup, ["object"] * 4)


def test_array() -> None:
    """Test rendering a schema with arrays of elements having their own schema"""
    soup = _generate_case("array")

    _assert_property_names(soup, ["fruits", "vegetables", "veggieName", "veggieLike"])
    _assert_descriptions(
        soup,
        [
            "A representation of a person, company, organization, or place",
            "The name of the vegetable.",
            "Do I like this vegetable?",
        ],
    )
    _assert_types(soup, ["object", "array of string", "string", "array", "object", "string", "boolean"])
    _assert_required(soup, [False, False, True, True])


def test_array_advanced():
    """Test rendering a schema that uses minItems, maxItems, and uniqueItems for arrays"""
    soup = _generate_case("array_advanced")

    _assert_descriptions(soup, ["A little food fun", "5 to 8 fruits that you like"])
    _assert_property_names(soup, ["fruits", "vegetables"])
    _assert_const(soup, ["eggplant"])
    _assert_required(soup, [False] * 2)


def test_with_definitions():
    """Test rendering a schema that uses the $ref keyword to refer to a definition attribute elsewhere in the schema"""
    soup = _generate_case("with_definitions")

    _assert_property_names(
        soup, ["billing_address", "street_address", "city", "state", "shipping_address"],
    )
    _assert_types(soup, ["object", "object", "string", "string", "string"])
    _assert_required(soup, [False, True, True, True, False])


def test_with_multiple_descriptions():
    """Test rendering a schema that uses multiple descriptions including with the $ref keyword"""
    soup = _generate_case("with_descriptions")

    _assert_descriptions(
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
    soup = _generate_case("combining_oneOf")

    _assert_one_of_options(soup, 4)
    _assert_types(soup, ["object"] * 5)
    _assert_required(soup, [True])


def test_combining_not():
    """Test rendering of the not schema attribute"""
    soup = _generate_case("combining_not")

    definitions = soup.find_all(class_="property-definition-div")
    assert len(definitions) == 1

    assert definitions[0].text.lstrip().startswith("Must not be:")


def test_with_default() -> None:
    """Test rendering of default values"""
    soup = _generate_case("with_default")

    _assert_default_values(soup, ['"Linux"', '["white", "blue"]', "2"])


def test_deprecated_in_description() -> None:
    """Test finding whether a property is deprecated from its description"""
    soup = _generate_case("deprecated", find_deprecated=True)

    _assert_property_names(soup, ["deprecated1", "deprecated2", "not_deprecated"])
    _assert_deprecated(soup, [True, True, False])


def test_deprecated_not_in_description() -> None:
    """Test that the deprecated badge does not get added if the option to get deprecated from description is disabled"""
    soup = _generate_case("deprecated", find_deprecated=False)

    _assert_deprecated(soup, [False] * 3)


def test_with_special_chars() -> None:
    soup = _generate_case("with_special_chars", find_deprecated=False)

    _assert_property_names(soup, ["prénom", "nomDeFamille", "âge", "0 de quoi d'autre"])

    buttons = soup.find_all("button", attrs={"aria-controls": True})
    expected_targets = ["#pr_nom", "#nomDeFamille", "#a_ge", "#a0_de_quoi_d_autre"]
    for i, expected_target in enumerate(expected_targets):
        assert buttons[i].attrs["data-target"] == expected_target


def test_description_with_ref() -> None:
    """Test that having a description next to a $ref in an object uses that description and not the one from the
    referenced object
    """
    soup = _generate_case("description_with_ref")

    _assert_descriptions(soup, ["We should see this", "inner description", "We should see this too"])


def test_description_from_ref() -> None:
    """Test that having a description next to a $ref in an object uses that description and not the one from the
    referenced object
    """
    soup = _generate_case("description_from_ref")

    _assert_descriptions(soup, ["a filled string"] * 2)


def test_description_with_ref_link_to_reused_ref() -> None:
    """Same as "test_description_with_ref", but do not allow reusing references."""
    soup = _generate_case("description_with_ref", link_to_reused_ref=False)

    _assert_descriptions(soup, ["We should see this", "inner description", "We should see this too"])


def test_with_examples() -> None:
    soup = _generate_case("with_examples")

    examples_label = soup.find_all("div", class_=["badge", "badge-secondary"])
    examples_label_text = [ex.text for ex in examples_label]
    assert examples_label_text == ["Examples:", "Example:", "Example:", "Example:"]

    examples_content = soup.find_all("div", class_="examples")
    examples_content_text = [ex.findChildren()[0].text for ex in examples_content]
    assert examples_content_text == [
        '"Guido"',
        '"BDFL"',
        '"Van Rossum"',
        "64",
        """{
    "birthplace": "Haarlem, Netherlands",
    "favorite_emoji": "🐍",
    "motto": "Beautiful is better than ugly.\\\\nExplicit is better than implicit.\\\\nSimple is better than complex.\\\\nComplex is better than complicated.\\\\nFlat is better than nested.\\\\nSparse is better than dense.\\\\nReadability counts.\\\\nSpecial cases aren't special enough to break the rules.\\\\nAlthough practicality beats purity.\\\\nErrors should never pass silently.\\\\nUnless explicitly silenced.\\\\nIn the face of ambiguity, refuse the temptation to guess.\\\\nThere should be one-- and preferably only one --obvious way to do it.\\\\nAlthough that way may not be obvious at first unless you're Dutch.\\\\nNow is better than never.\\\\nAlthough never is often better than *right* now.\\\\nIf the implementation is hard to explain, it's a bad idea.\\\\nIf the implementation is easy to explain, it may be a good idea.\\\\nNamespaces are one honking great idea -- let's do more of those!"
}""",
    ]


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_recursive(link_to_reused_ref: bool) -> None:
    """Test a schema having a recursive definition"""
    soup = _generate_case("recursive", link_to_reused_ref=link_to_reused_ref)

    _assert_descriptions(soup, ["A human being", "The children they had", "A human being"])

    recursive_definition_link = soup.find("a", href="#person")
    assert recursive_definition_link
    assert recursive_definition_link.text == "Same definition as person"


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_recursive_array(link_to_reused_ref: bool) -> None:
    """Test a schema having a recursive definition pointing to array items"""
    soup = _generate_case("recursive_array", link_to_reused_ref=link_to_reused_ref)

    _assert_descriptions(soup, ["A list of people", "A human being", "The children they had", "A human being"])

    recursive_definition_link = soup.find("a", href="#person_items")
    assert recursive_definition_link
    assert recursive_definition_link.text == "Same definition as person_items"


def test_pattern_properties() -> None:
    soup = _generate_case("pattern_properties")

    pattern_label = soup.find_all("span", class_=["badge-info"])
    pattern_label_text = [ex.text for ex in pattern_label]
    assert pattern_label_text == ["Pattern Property"]

    pattern_content = soup.find_all("span", class_="pattern-value")
    pattern_content_text = [ex.findChildren()[0].text for ex in pattern_content]
    assert pattern_content_text == ["$[a-c][0-9]^"]

    _assert_property_names(soup, ["firstName", "lastName", "paperSize", "rating", "review"])

    _assert_descriptions(
        soup,
        [
            "The person's first name.",
            "The person's last name.",
            "Review of a paper size.",
            "Numerical rating for paper size.",
            "Narrative review of the paper size.",
        ],
    )


def test_conditional_subschema() -> None:
    soup = _generate_case("conditional_subschema")

    _assert_types(
        soup, ["object", "object", "const", "object", "object", "object", "object", "string", "enum (of string)"]
    )


def test_html_in_patterns() -> None:
    soup = _generate_case("html_in_patterns")

    code_blocks = soup.find_all("code")
    assert list(block.text for block in code_blocks) == [
        "^(<<variable:([-+/*0-9A-Za-z_]+)>>|<<auto>>)$",
        "$[a-c][0-9]^<a>",
    ]

    _assert_property_names(soup, ["$[a-c][0-9]^<a>"])


def test_yaml() -> None:
    """Test loading the schema from a YAML file. The schema is the same as the case "with_definitions"."""
    with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "cases", f"yaml.yaml"))) as schema_fp:
            generate_from_file_object(schema_fp, temp_file, True, False, False, True)

        temp_file.seek(0)
        soup = BeautifulSoup(temp_file.read(), "html.parser")

    # Order of properties is only preserved in Python 3.7+
    _assert_property_names(
        soup, ["billing_address", "street_address", "city", "state", "shipping_address"],
    )
    _assert_types(soup, ["object", "object", "string", "string", "string"])
    _assert_required(soup, [False, True, True, True, False])
