import os

from json_schema_for_humans.generate import build_intermediate_representation
from tests.test_utils import _get_test_case_path


def test_basic() -> None:
    intermediate = build_intermediate_representation(_get_test_case_path("basic"))

    assert intermediate


def test_references() -> None:
    intermediate = build_intermediate_representation(_get_test_case_path("references"))

    assert intermediate
