"""Run this to populate the example cases from the code to Jekyll folder"""

import os
import shutil
import sys

templateName="js"
if len( sys.argv ) >= 2:
    print(sys.argv)
    templateName=sys.argv[1]

templateExtension="html"
if templateName == 'md':
    templateExtension="md"

sys.path.insert(0, os.path.abspath(".."))

from json_schema_for_humans.generate import generate_from_filename, GenerationConfiguration

cases_source_dir = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), "tests", "cases"))
includes_dir = os.path.join(os.getcwd(), "_includes")
json_examples_dir = os.path.join(os.getcwd(), "_includes", "examples")
os.makedirs(json_examples_dir, exist_ok=True)
asserts_dir = os.path.join(os.getcwd(), "assets")
results_example_dir = os.path.join(asserts_dir, f"examples_{templateName}")
os.makedirs(results_example_dir, exist_ok=True)


readme = "README.md"
readme_location = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), readme))
shutil.copyfile(readme_location, os.path.join(includes_dir, readme))

config_schema = "config_schema.json"
config_schema_location = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), config_schema))
generate_from_filename(config_schema_location, os.path.join(asserts_dir, "config_schema.html"), expand_buttons=True)
configMd = GenerationConfiguration(deprecated_from_description=True, template_name="md")
generate_from_filename(config_schema_location, os.path.join(asserts_dir, "config_schema.md"), config=configMd)

config = GenerationConfiguration(
    deprecated_from_description=True, 
    expand_buttons=True, 
    template_name=templateName,
    template_md_options={ "badge_as_image": False }   
)

for case_name in os.listdir(cases_source_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(cases_source_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue

    print(f"Generating example {name}")
    #if(name == 'array_advanced'):
    generate_from_filename(case_source, os.path.join(results_example_dir, f"{name}.{templateExtension}"), config=config)
