from json_schema_for_humans.generate import GenerationConfiguration, build_intermediate_representation
from tests.test_utils import get_test_case_path


def test_basic() -> None:
    intermediate = build_intermediate_representation(get_test_case_path("basic"), GenerationConfiguration())

    assert intermediate


def test_references() -> None:
    intermediate = build_intermediate_representation(get_test_case_path("references"), GenerationConfiguration())

    assert intermediate
