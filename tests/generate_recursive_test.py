import pytest

from json_schema_for_humans.generate import GenerationConfiguration
from tests.html_schema_doc_asserts import assert_descriptions, assert_ref_link, get_ref_link
from tests.test_utils import generate_case


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_recursive(link_to_reused_ref: bool) -> None:
    """Test a schema having a recursive definition.

    Even if `link_to_reused_ref` is False, a reference will be generated to avoid a RecursionError
    """
    soup = generate_case("recursive", GenerationConfiguration(link_to_reused_ref=link_to_reused_ref))

    assert_descriptions(soup, ["A human being", "The children they had", "A human being"])

    assert_ref_link(soup, "#person", "Same definition as person")


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_recursive_parent_in_definition(link_to_reused_ref: bool) -> None:
    """Test a schema having a recursive definition. Moreover, the ref is linked to an attribute in a definition that
    has not been seen in the tree before

    Even if `link_to_reused_ref` is False, a reference will be generated to avoid a RecursionError
    """
    soup = generate_case(
        "recursive_parent_in_definition", GenerationConfiguration(link_to_reused_ref=link_to_reused_ref)
    )

    assert_descriptions(
        soup,
        [
            "Relationships between this person and others",
            "A human being",
            "Relationships between this person and others",
            "A human being",
        ],
    )

    assert_ref_link(soup, "#relationships_mother", "Same definition as mother")


def test_recursive_array() -> None:
    """Test a schema having a recursive definition pointing to array items"""
    soup = generate_case("recursive_array", GenerationConfiguration(link_to_reused_ref=True))

    assert_descriptions(soup, ["A list of people", "A human being", "The children they had", "A human being"])

    assert_ref_link(soup, "#person_items", "Same definition as person")


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_recursive_two_files(link_to_reused_ref: bool) -> None:
    """Test rendering a schema with a recursive definition with the same name, but in another file"""
    soup = generate_case("recursive_two_files", GenerationConfiguration(link_to_reused_ref=link_to_reused_ref))

    assert_descriptions(
        soup,
        [
            "A human being",
            "The children they had",
            "Person definition from second file. Not the same!",
            "Person definition from second file. Not the same!",
        ],
    )

    if link_to_reused_ref:
        assert_ref_link(soup, "#person_siblings", "Same definition as siblings")
    else:
        assert not get_ref_link(soup, "#person_siblings")
