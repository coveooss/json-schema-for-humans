"""Run this to populate the example cases from the code to Jekyll folder"""

import os
import shutil
import sys

templateName="js"
templateExtension="html"
if len( sys.argv ) >= 2:
    print(sys.argv)
    templateName=sys.argv[1]

if templateName == 'md':
    print("please use tests/generate_expected_md.py instead")
    sys.exit()

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from json_schema_for_humans.generate import generate_from_filename, GenerationConfiguration

cases_source_dir = os.path.abspath(os.path.join(parent_dir, "tests", "cases"))
includes_dir = os.path.join(current_dir, "_includes")

# copy json example files
json_examples_dir = os.path.join(includes_dir, "examples")
os.makedirs(json_examples_dir, exist_ok=True)
shutil.copytree(cases_source_dir, json_examples_dir, dirs_exist_ok=True)

asserts_dir = os.path.join(current_dir, "assets")
results_example_dir = os.path.join(asserts_dir, f"examples_{templateName}")
os.makedirs(results_example_dir, exist_ok=True)

readme = "README.md"
readme_location = os.path.abspath(os.path.join(parent_dir, readme))
shutil.copyfile(readme_location, os.path.join(includes_dir, readme))

config_schema = "config_schema.json"
config_schema_location = os.path.abspath(os.path.join(parent_dir, config_schema))
generate_from_filename(config_schema_location, os.path.join(asserts_dir, "config_schema.html"), expand_buttons=True)

config_schema_md = "config_schema.md"
config_md = GenerationConfiguration(deprecated_from_description=True, template_name="md")
config_md_location = os.path.join(asserts_dir, config_schema_md)
generate_from_filename(config_schema_location, config_md_location, config=config_md)
shutil.copyfile(config_md_location, os.path.join(includes_dir, config_schema_md))

config = GenerationConfiguration(
    deprecated_from_description=True, 
    expand_buttons=True, 
    template_name=templateName
)

for case_name in os.listdir(cases_source_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(cases_source_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue

    print(f"Generating example {name}")
    #if(name == 'array_advanced'):
    generate_from_filename(case_source, os.path.join(results_example_dir, f"{name}.{templateExtension}"), config=config)
