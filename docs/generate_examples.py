"""Run this to populate the example cases from the code to Jekyll folder"""

import os
import shutil
import sys

sys.path.insert(0, os.path.abspath(".."))

from json_schema_for_humans.generate import generate_from_filename

cases_source_dir = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), "tests", "cases"))
cases_dest_dir = os.path.join(os.getcwd(), "_includes", "examples")
os.makedirs(cases_dest_dir, exist_ok=True)
results_dest_dir = os.path.join(os.getcwd(), "assets", "examples")
os.makedirs(results_dest_dir, exist_ok=True)


for case_name in os.listdir(cases_source_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(cases_source_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue

    shutil.copyfile(case_source, os.path.join(cases_dest_dir, case_name))

    print(f"Generating example {name}")

    generate_from_filename(
        case_source, os.path.join(results_dest_dir, f"{name}.html"), deprecated_from_description=True
    )
