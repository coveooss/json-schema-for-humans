import os

from json_schema_for_humans.generate import generate_from_schema
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from tests.test_utils import get_test_case_path
import re

GENERATED_TIMESTAMP_REGEXP = re.compile(
    r"on [0-9]{4}-[0-9]{2}-[0-9]{2} at [0-9]{2}:[0-9]{2}:[0-9]{2} \+[0-9]{4}", re.IGNORECASE | re.MULTILINE
)


class MdUtilsAsserts:
    def get_expected_test_case_path(self, example_dir: str, name: str) -> str:
        """Get the expected md for a test case"""
        return os.path.realpath(os.path.join(example_dir, f"{name}.md"))

    def generate_case(self, case_name: str, config: GenerationConfiguration = None) -> str:
        """Get the generated markdown schema string for a given schema test case"""
        return generate_from_schema(get_test_case_path(case_name), None, config=config)

    def get_expected_case(self, example_dir: str, test_case: str, case_name: str) -> str:
        """Get the content of expected_md/test_case/case_name.md - containing expected result"""
        with open(
            self.get_expected_test_case_path(example_dir, os.path.join(test_case, case_name)), "r", encoding="utf-8"
        ) as f:
            content = f.read()

        return content

    def assert_case_equals(
        self, example_dir: str, test_case: str, case_name: str, config: GenerationConfiguration = None
    ) -> None:
        content = self.generate_case(case_name, config)
        expected_content = self.get_expected_case(example_dir, test_case, case_name)

        # remove generated date on both contents
        regexp = r"^(Generated using \[json-schema-for-humans\]\(https:[^)]+\) on) (.+)$"
        content = re.sub(regexp, r"\1 date", content, flags=re.MULTILINE)

        assert expected_content == content
