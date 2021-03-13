"""Run this to populate the example cases from the code to Jekyll folder"""
import os
import sys
import re

# init directories
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from pprint import pprint

from json_schema_for_humans.generate import GenerationConfiguration, generate_from_filename

template_names = ["js", "flat", "md"]
template_extension = "html"
if len(sys.argv) >= 2:
    template_names = [sys.argv[1]]


examples_dir = os.path.join(current_dir, "examples")
json_examples_dir = os.path.join(examples_dir, "cases")

config_md = GenerationConfiguration(
    template_name = "md", 
    deprecated_from_description=True
)

configurations = {
    "js": {
        "default": GenerationConfiguration(
            template_name = 'js',
            deprecated_from_description=True, 
            expand_buttons = True
        ),
    },
    "flat": {
        "default": GenerationConfiguration(
            template_name = 'flat',
            deprecated_from_description=True, 
            expand_buttons = True
        ),
    },
    "md": {
        "default": GenerationConfiguration(
            template_name = "md", 
            deprecated_from_description=True
        ),
        "with_badges": GenerationConfiguration(
            template_name = "md", 
            deprecated_from_description=True,
            template_md_options={"badge_as_image": True}
        )
    }
}

GENERATED_TIMESTAMP_REGEXP = re.compile(r"on [0-9]{4}-[0-9]{2}-[0-9]{2} at [0-9]{2}:[0-9]{2}:[0-9]{2} \+[0-9]{4}", re.IGNORECASE)

def remove_generated_timestamp(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        last_line = GENERATED_TIMESTAMP_REGEXP.sub('on date', lines.pop())
        lines.append(last_line)
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def generate_each_template(configurations, template_names, json_case_filename, dest_dir):
    """ 
    generate example from json case file for each template selected
    """
    dest_name = os.path.basename(json_case_filename)
    
    for template_name, template_configurations in configurations.items():
        if not(template_name in template_names):
            continue
        for config_name, template_configuration in template_configurations.items():
            example_dest_dir = os.path.join(dest_dir, "examples_" + template_name + "_" + config_name)
            os.makedirs(example_dest_dir, exist_ok=True)
            example_file_name = dest_name + (".md" if template_name == "md" else ".html")
            example_file_path = os.path.join(example_dest_dir, example_file_name)
            generate_from_filename(
                config_schema_location, 
                example_file_path,
                config = template_configuration
            )
            remove_generated_timestamp(example_file_path)

config_schema = "config_schema.json"
config_schema_location = os.path.abspath(os.path.join(parent_dir, config_schema))
generate_each_template(configurations, template_names, config_schema_location, examples_dir)

for case_name in os.listdir(json_examples_dir):
    name, ext = os.path.splitext(case_name)
    case_source = os.path.abspath(os.path.join(json_examples_dir, case_name))
    if not os.path.isfile(case_source) or ext != ".json":
        continue

    print(f"Generating example {name}")
    generate_each_template(
        configurations, 
        template_names, 
        case_source,
        examples_dir
    )
