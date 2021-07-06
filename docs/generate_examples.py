"""Run this to populate the example cases from the code to Jekyll folder"""
import os
import sys
import re
from typing import TextIO

import yaml

# init directories
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

template_names = ["js", "flat", "md", "md_nested"]
template_extension = "html"
if len(sys.argv) >= 2:
    template_names = [sys.argv[1]]


examples_dir = os.path.join(current_dir, "examples")
json_examples_dir = os.path.join(examples_dir, "cases")

config_md = GenerationConfiguration(template_name="md", deprecated_from_description=True)

EXAMPLES_HEADER_TEMPLATE = """
# {title} <!-- {{docsify-ignore-all}} -->

<!-- select:start -->
<!-- select-menu-labels: Schema -->

Here you can browse various example schemas and their rendition with several templates.

"""

CONFIGURATION_HEADER_TEMPLATE = """
# {title} <!-- {{docsify-ignore-all}} -->

<!-- select:start -->
<!-- select-menu-labels: Schema -->

Here you will find the JSON schema and generated doc for the generation configuration.

These parameters can be provided with a json or yaml file, through the CLI, or through a `GenerationConfiguration` object if calling by code.

"""


EXAMPLES_FOOTER_TEMPLATE = """

<!-- select:end -->
"""

MD_EXAMPLE_JSON_TEMPLATE = """

<details>
<summary>{title} - Click here to expand source code...</summary>

[{file_url}]({file_url} ':include :type=code')
</details>
"""
MD_EXAMPLE_JS_TEMPLATE = """

<details>
<summary>{title} - Click here to expand the rendered result...</summary>
<a href="https://coveooss.github.io/json-schema-for-humans/{file_url}" target="_blank">Open it in full page</a>

[{file_url}]({file_url} ':include :type=iframe width=100% height=400px')
</details>
"""
MD_EXAMPLE_MD_TEMPLATE = """

<details>
<summary>{title} - Click here to expand the rendered result...</summary>
<a href="https://github.com/coveooss/json-schema-for-humans/blob/master/docs/{file_url}" target="_blank">Open it in github</a>

[{file_url}]({file_url} ':include')
</details>
"""

configurations = [
    {
        "title": "JS template",
        "dir_name": "examples_js_default",
        "config": GenerationConfiguration(
            minify=False, template_name="js", deprecated_from_description=True, expand_buttons=True
        ),
        "md_example_template": MD_EXAMPLE_JS_TEMPLATE,
    },
    {
        "title": "Flat template",
        "dir_name": "examples_flat_default",
        "config": GenerationConfiguration(
            minify=False, template_name="flat", deprecated_from_description=True, expand_buttons=True
        ),
        "md_example_template": MD_EXAMPLE_JS_TEMPLATE,
    },
    {
        "title": "Markdown without badge template",
        "dir_name": "examples_md_default",
        "config": GenerationConfiguration(template_name="md", deprecated_from_description=True),
        "md_example_template": MD_EXAMPLE_MD_TEMPLATE,
    },
    {
        "title": "Markdown with badges template",
        "dir_name": "examples_md_with_badges",
        "config": GenerationConfiguration(
            template_name="md", deprecated_from_description=True, template_md_options={"badge_as_image": True}
        ),
        "md_example_template": MD_EXAMPLE_MD_TEMPLATE,
    },
    {
        "title": "Nested Markdown without badges template",
        "dir_name": "examples_md_nested_default",
        "config": GenerationConfiguration(
            template_name="md_nested", deprecated_from_description=True, template_md_options={"badge_as_image": False}
        ),
        "md_example_template": MD_EXAMPLE_MD_TEMPLATE,
    },
    {
        "title": "Nested Markdown with badges template",
        "dir_name": "examples_md_nested_with_badges",
        "config": GenerationConfiguration(
            template_name="md_nested", deprecated_from_description=True, template_md_options={"badge_as_image": True}
        ),
        "md_example_template": MD_EXAMPLE_MD_TEMPLATE,
    },
]

with open(
    os.path.realpath(os.path.join(current_dir, "cases_description.yaml")), encoding="utf-8"
) as cases_description_fp:
    CASES_DESCRIPTION_DICT = yaml.safe_load(cases_description_fp.read())

GENERATED_TIMESTAMP_REGEXP = re.compile(r"on \d{4}-\d{2}-\d{2} at \d{2}:\d{2}:\d{2} [+-]\d{4}", re.IGNORECASE)


def remove_generated_timestamp(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        last_line = GENERATED_TIMESTAMP_REGEXP.sub("on date", lines.pop())
        lines.append(last_line)
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


config_schema = "config_schema.json"
config_schema_location = os.path.abspath(os.path.join(parent_dir, config_schema))


def generate_each_template(
    examples_md_file, configurations, template_names, case_path, case_url, case_name, examples_dir
) -> None:
    """
    Generate examples from JSON case file for each template selected
    """
    print(f"Generating example {case_name}")

    examples_md_file.write(f"\n## --{case_name}--")
    if case_name in CASES_DESCRIPTION_DICT:
        case_data = CASES_DESCRIPTION_DICT[case_name]
        case_display_name = case_data["display_name"]
        case_description = case_data["description"]
        examples_md_file.write(f"\n### {case_display_name}\n\n")
        if case_description:
            examples_md_file.write(f"**Description:** {case_description}\n")
    else:
        examples_md_file.write(f"\n### {case_name}\n")

    examples_md_file.write(MD_EXAMPLE_JSON_TEMPLATE.format(file_url=case_url, title="Json schema"))
    for config in configurations:
        template_configuration = config["config"]
        template_name = template_configuration.template_name
        example_dir_name = config["dir_name"]
        example_file_name = case_name + (".md" if template_name in ("md", "md_nested") else ".html")

        examples_md_file.write(
            config["md_example_template"].format(
                file_url=f"examples/{example_dir_name}/{example_file_name}", title=config["title"]
            )
        )
        if not (template_name in template_names):
            continue

        example_dest_dir = os.path.join(examples_dir, example_dir_name)
        os.makedirs(example_dest_dir, exist_ok=True)

        example_file_path = os.path.join(example_dest_dir, example_file_name)
        generate_from_filename(case_path, example_file_path, config=template_configuration)
        remove_generated_timestamp(example_file_path)


def generate_examples(examples_md_file: TextIO):
    for case_name in sorted(os.listdir(json_examples_dir)):
        name, ext = os.path.splitext(case_name)
        case_source = os.path.abspath(os.path.join(json_examples_dir, case_name))
        if not os.path.isfile(case_source) or ext != ".json":
            continue

        generate_each_template(
            examples_md_file,
            configurations,
            template_names,
            case_source,
            os.path.relpath(case_source, current_dir).replace("\\", "/"),
            name,
            examples_dir,
        )


# generate examples
examples_md_file_path = os.path.join(current_dir, "Examples.md")
with open(examples_md_file_path, "w", encoding="utf-8") as examples_md_file:
    examples_md_file.write(EXAMPLES_HEADER_TEMPLATE.format(title="Examples"))
    generate_examples(examples_md_file)
    examples_md_file.write(EXAMPLES_FOOTER_TEMPLATE)

# generate configuration files
configuration_md_file_path = os.path.join(current_dir, "Configuration.md")
with open(configuration_md_file_path, "w", encoding="utf-8") as configuration_md_file:
    configuration_md_file.write(CONFIGURATION_HEADER_TEMPLATE.format(title="Configuration"))
    generate_each_template(
        configuration_md_file,
        configurations,
        template_names,
        config_schema_location,
        f"/{config_schema}",
        "Configuration",
        examples_dir,
    )
    configuration_md_file.write(EXAMPLES_FOOTER_TEMPLATE)
