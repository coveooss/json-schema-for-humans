import pytest

from tests.test_utils import generate_case
from tests.html_schema_doc_asserts import assert_descriptions


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_recursive(link_to_reused_ref: bool) -> None:
    """Test a schema having a recursive definition.

    Even if `link_to_reused_ref` is False, a reference will be generated to avoid a RecursionError
    """
    soup = generate_case("recursive", link_to_reused_ref=link_to_reused_ref)

    assert_descriptions(soup, ["A human being", "The children they had", "A human being"])

    recursive_definition_link = soup.find("a", href="#person")
    assert recursive_definition_link
    assert recursive_definition_link.text == "Same definition as person"


def test_recursive_array() -> None:
    """Test a schema having a recursive definition pointing to array items"""
    soup = generate_case("recursive_array", link_to_reused_ref=True)

    assert_descriptions(soup, ["A list of people", "A human being", "The children they had", "A human being"])

    recursive_definition_link = soup.find("a", href="#person_items")
    assert recursive_definition_link
    assert recursive_definition_link.text == "Same definition as person"


@pytest.mark.parametrize("link_to_reused_ref", [True, False])
def test_recursive_two_files(link_to_reused_ref: bool) -> None:
    """Test rendering a schema with a recursive definition with the same name, but in another file"""
    soup = generate_case("recursive_two_files", link_to_reused_ref=link_to_reused_ref)

    assert_descriptions(
        soup,
        [
            "A human being",
            "The children they had",
            "Person definition from second file. Not the same!",
            "Person definition from second file. Not the same!",
        ],
    )

    recursive_definition_link = soup.find("a", href="#person_siblings")
    if link_to_reused_ref:
        assert recursive_definition_link
        assert recursive_definition_link.text == "Same definition as siblings"
    else:
        assert not recursive_definition_link
