import os

from json_schema_for_humans.generate import generate_from_schema, GenerationConfiguration
from tests.test_utils import get_test_case_path
import re


class MdUtilsAsserts:
    def get_expected_test_case_path(self, name: str) -> str:
        """Get the expected md for a test case"""
        return os.path.realpath(os.path.join(os.path.dirname(__file__), "expected_md", f"{name}.md"))

    def generate_case(self, case_name: str, config: GenerationConfiguration = None) -> str:
        """Get the generated markdown schema string for a given schema test case"""
        return generate_from_schema(get_test_case_path(case_name), None, config=config)

    def get_expected_case(self, test_case: str, case_name: str) -> str:
        """Get the content of expected_md/test_case/case_name.md - containing expected result"""
        with open(self.get_expected_test_case_path(os.path.join(test_case, case_name)), "r") as f:
            content = f.read()

        return content

    def assert_case_equals(self, test_case: str, case_name: str, config: GenerationConfiguration = None) -> None:
        content = self.generate_case(case_name, config)
        expectedContent = self.get_expected_case(test_case, case_name)
        # remove generation date on both contents
        regexp = r"^(Generated using \[json-schema-for-humans\]\(https:[^)]+\) on) (.+)$"
        content = re.sub(regexp, content, r"\1 date")

        assert expectedContent == content
