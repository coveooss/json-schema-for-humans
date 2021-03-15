import os
import pytest

from json_schema_for_humans.generate import GenerationConfiguration
from tests.md_utils_asserts import MdUtilsAsserts

configBadge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": True})
configNoBadge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": False})
testCases = []
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
example_dir = os.path.join(parent_dir, "docs", "examples")
cases_source_dir = os.path.join(example_dir, "cases")

for case_name in os.listdir(cases_source_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(cases_source_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue
    testCases.append(("examples_md_default", name, configNoBadge))
    testCases.append(("examples_md_with_badges", name, configBadge))
    break


class TestMdGenerate(MdUtilsAsserts):
    @pytest.mark.parametrize("testCase, template, config", testCases)
    def test_basic(self, testCase, template, config):
        """Test rendering a basic schema with title"""
        self.assert_case_equals(example_dir, testCase, template, config)
