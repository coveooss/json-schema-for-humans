"""Run this to populate the expected md cases from the cases folder"""

import os
import sys
from pprint import pprint

sys.path.insert(0, os.path.abspath(".."))

from json_schema_for_humans.generate import generate_from_filename, GenerationConfiguration

cases_source_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "cases"))
with_badge_dir = os.path.join(os.path.dirname(__file__), "expected_md", "with_badge")
os.makedirs(with_badge_dir, exist_ok=True)
without_badge_dir = os.path.join(os.path.dirname(__file__), "expected_md", "without_badge")
os.makedirs(with_badge_dir, exist_ok=True)

configWithBadge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": True})
configWithoutBadge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": False})
for case_name in os.listdir(cases_source_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(cases_source_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue

    print(f"Generating expected {name}")
    generate_from_filename(case_source, os.path.join(with_badge_dir, f"{name}.md"), config=configWithBadge)
    generate_from_filename(case_source, os.path.join(without_badge_dir, f"{name}.md"), config=configWithoutBadge)
