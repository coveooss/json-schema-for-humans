import os
import pytest

from json_schema_for_humans.generate import GenerationConfiguration
from tests.md_utils_asserts import MdUtilsAsserts

configBadge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": True})
configNoBadge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": False})
testCases = []
cases_source_dir = os.path.join(os.path.dirname(__file__), "cases")

for case_name in os.listdir(cases_source_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(cases_source_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue
    testCases.append(("with_badge", name, configBadge))
    testCases.append(("without_badge", name, configNoBadge))


class TestMdGenerate(MdUtilsAsserts):
    @pytest.mark.parametrize("testCase, template, config", testCases)
    def test_basic(self, testCase, template, config):
        """Test rendering a basic schema with title"""
        self.assert_case_equals(testCase, template, config)
