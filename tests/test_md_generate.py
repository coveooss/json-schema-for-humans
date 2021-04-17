import os
from typing import List
import pytest
from dataclasses import dataclass
from pathlib import Path

from json_schema_for_humans.generation_configuration import GenerationConfiguration
from tests.md_utils_asserts import MdUtilsAsserts

config_badge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": True})
config_no_badge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": False})


@dataclass
class TestCase:
    name: str
    config: GenerationConfiguration


def list_cases() -> List[str]:
    test_cases: List[str] = []
    for case_file_path in (Path(__file__).parent / "cases").iterdir():
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
            "with_badge" if with_badge else "without_badge",
            test_case,
            GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": with_badge}),
        )
