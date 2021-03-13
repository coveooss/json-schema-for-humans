"""Run this to populate the expected md cases from the cases folder"""

import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from json_schema_for_humans.generate import generate_from_filename, GenerationConfiguration


def remove_generated_timestamp(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = lines[:-1]
        lines.append(
            "Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date"
        )
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


cases_source_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "cases"))
doc_examples_dir = os.path.join(parent_dir, "docs", "_includes")
with_badge_dir = os.path.join(doc_examples_dir, "examples_md_with_badge")
os.makedirs(with_badge_dir, exist_ok=True)
without_badge_dir = os.path.join(doc_examples_dir, "examples_md_without_badge")
os.makedirs(without_badge_dir, exist_ok=True)

config_with_badge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": True})
config_without_badge = GenerationConfiguration(template_name="md", template_md_options={"badge_as_image": False})
for case_name in os.listdir(cases_source_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(cases_source_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue

    print(f"Generating expected {name}")
    f = os.path.join(with_badge_dir, f"{name}.md")
    generate_from_filename(case_source, f, config=config_with_badge)
    remove_generated_timestamp(f)

    f = os.path.join(without_badge_dir, f"{name}.md")
    generate_from_filename(case_source, f, config=config_without_badge)
    remove_generated_timestamp(f)
