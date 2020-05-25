import os

from json_schema_for_humans.generate import build_intermediate_representation


def _get_test_case_path(name: str) -> str:
    """Get the loaded JSON schema for a test case"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "cases", f"{name}.json"))


def test_basic() -> None:
    intermediate = build_intermediate_representation(_get_test_case_path("basic"))

    assert intermediate


def test_references() -> None:
    intermediate = build_intermediate_representation(_get_test_case_path("references"))

    assert intermediate
