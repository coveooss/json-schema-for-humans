import os
from typing import List
import pytest
from dataclasses import dataclass
from pathlib import Path

from json_schema_for_humans.generation_configuration import GenerationConfiguration
from tests.md_utils_asserts import MdUtilsAsserts

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.dirname(current_dir))
examples_dir = os.path.join(parent_dir, "docs", "examples")

config_badge = GenerationConfiguration(
    template_name="md", template_md_options={"badge_as_image": True}, deprecated_from_description=True
)
config_no_badge = GenerationConfiguration(
    template_name="md", template_md_options={"badge_as_image": False}, deprecated_from_description=True
)


@dataclass
class TestCase:
    name: str
    config: GenerationConfiguration

    __test__ = False


def list_cases() -> List[str]:
    test_cases: List[str] = []
    for case_file_path in (Path(os.path.join(examples_dir, "cases"))).iterdir():
        if not (case_file_path.is_file() and case_file_path.exists() and case_file_path.name.endswith(".json")):
            continue
        test_cases.append(os.path.splitext(case_file_path.name)[0])
    return test_cases


class TestMdGenerate(MdUtilsAsserts):
    @pytest.mark.parametrize("test_case", list_cases())
    @pytest.mark.parametrize("with_badge", [True, False])
    def test_basic(self, test_case: str, with_badge: bool):
        """Test rendering a basic schema with title"""
        self.assert_case_equals(
            examples_dir,
            "examples_md_with_badges" if with_badge else "examples_md_default",
            test_case,
            config_badge if with_badge else config_no_badge,
        )
