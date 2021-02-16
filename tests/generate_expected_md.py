"""Run this to populate the expected md cases from the cases folder"""

import os
import sys
from pprint import pprint

sys.path.insert(0, os.path.abspath(".."))

def removeGeneratedTimestamp(filePath: str) -> None:
    with open(filePath, 'r') as f:
        lines = f.readlines()
        lines = lines[:-1]
        lines.append('Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date')
    with open(filePath, 'w') as f:
        f.writelines(lines)
    
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
    f=os.path.join(with_badge_dir, f"{name}.md")
    generate_from_filename(case_source, f, config=configWithBadge)
    removeGeneratedTimestamp(f)

    f = os.path.join(without_badge_dir, f"{name}.md")
    generate_from_filename(case_source, f, config=configWithoutBadge)
    removeGeneratedTimestamp(f)
