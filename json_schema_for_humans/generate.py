import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, TextIO, Union

import click
import htmlmin
import jinja2
import markdown2
from jinja2 import FileSystemLoader
from jinja2.ext import loopcontrols

from json_schema_for_humans import jinja_filters, templating_utils
from json_schema_for_humans.generation_configuration import GenerationConfiguration, _get_final_config
from json_schema_for_humans.intermediate_representation import build_intermediate_representation
from json_schema_for_humans.md_template import MarkdownTemplate

TEMPLATE_FILE_NAME = "base.html"
CSS_FILE_NAME = "schema_doc.css"
JS_FILE_NAME = "schema_doc.min.js"


def generate_from_schema(
    schema_file: Union[str, Path, TextIO],
    loaded_schemas: Optional[Dict[str, Any]] = None,
    minify: bool = True,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    link_to_reused_ref: bool = True,
    config: GenerationConfiguration = None,
) -> str:
    config = config or _get_final_config(
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        copy_css=False,
        copy_js=False,
        link_to_reused_ref=link_to_reused_ref,
    )

    templates_directory = os.path.join(config.templates_directory, config.template_name)
    base_template_path = os.path.join(templates_directory, TEMPLATE_FILE_NAME)

    loader = FileSystemLoader(templates_directory)
    env = jinja2.Environment(
        loader=loader,
        extensions=[loopcontrols],
        trim_blocks=(config.template_name in ("md", "md_nested")),
        lstrip_blocks=(config.template_name in ("md", "md_nested")),
    )
    env.globals["jsfh_config"] = config
    env.globals["jsfh_md"] = markdown2.Markdown(extras=config.markdown_options)
    if config.template_name in ("md", "md_nested"):
        md_template = MarkdownTemplate(config)
        md_template.register_jinja(env)

    env.filters["python_to_json"] = jinja_filters.python_to_json
    env.filters["get_default"] = (
        jinja_filters.get_default_look_in_description if config.default_from_description else jinja_filters.get_default
    )
    env.filters["get_type_name"] = templating_utils.get_type_name
    env.filters["get_description"] = jinja_filters.get_description
    env.filters["get_numeric_restrictions_text"] = jinja_filters.get_numeric_restrictions_text

    env.filters["get_required_properties"] = jinja_filters.get_required_properties
    env.filters["get_first_property"] = jinja_filters.get_first_property
    env.filters["get_undocumented_required_properties"] = jinja_filters.get_undocumented_required_properties
    env.filters["highlight_json_example"] = jinja_filters.highlight_json_example
    env.filters["highlight_yaml_example"] = jinja_filters.highlight_yaml_example
    env.filters["first_line"] = jinja_filters.first_line

    env.tests["combining"] = jinja_filters.is_combining
    env.tests["description_short"] = jinja_filters.is_text_short
    env.tests["deprecated"] = lambda schema: jinja_filters.deprecated(config, schema)
    env.globals["examples_as_yaml"] = config.examples_as_yaml
    env.globals["get_local_time"] = jinja_filters.get_local_time

    with open(base_template_path, "r") as template_fp:
        template = env.from_string(template_fp.read())

    if isinstance(schema_file, list):
        # Backward compatibility
        schema_file = os.path.sep.join(schema_file)

    intermediate_schema = build_intermediate_representation(schema_file, config, loaded_schemas)

    rendered = template.render(schema=intermediate_schema, config=config)

    if minify:
        if config.is_markdown_template:
            # remove multiple contiguous empty lines
            rendered = re.sub(r"\n\s*\n", "\n\n", rendered)
        else:
            rendered = htmlmin.minify(rendered)

    return rendered


def generate_from_filename(
    schema_file_name: Union[str, Path],
    result_file_name: str,
    minify: bool = True,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    copy_css: bool = True,
    copy_js: bool = True,
    link_to_reused_ref: bool = True,
    config: GenerationConfiguration = None,
) -> None:
    """Generate the schema documentation from a filename"""
    config = config or _get_final_config(
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        copy_css=copy_css,
        copy_js=copy_js,
        link_to_reused_ref=link_to_reused_ref,
    )

    if isinstance(schema_file_name, str):
        schema_file_name = os.path.realpath(schema_file_name)
    elif isinstance(schema_file_name, Path):
        schema_file_name = str(schema_file_name.resolve())

    if not os.path.exists(os.path.dirname(os.path.realpath(result_file_name))):
        raise FileNotFoundError(
            f"Output directory {os.path.dirname(os.path.realpath(result_file_name))} does not exist"
        )

    rendered_schema_doc = generate_from_schema(
        schema_file_name,
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        link_to_reused_ref=link_to_reused_ref,
        config=config,
    )

    copy_css_and_js_to_target(result_file_name, config)

    with open(result_file_name, "w", encoding="utf-8") as result_schema_doc:
        result_schema_doc.write(rendered_schema_doc)


def generate_from_file_object(
    schema_file: TextIO,
    result_file: TextIO,
    minify: bool = True,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    copy_css: bool = True,
    copy_js: bool = True,
    link_to_reused_ref: bool = True,
    config: GenerationConfiguration = None,
) -> None:
    """Generate the JSON schema documentation from opened file objects for both input and output files. The
    result_file should be opened in write mode.
    """
    config = config or _get_final_config(
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        copy_css=copy_css,
        copy_js=copy_js,
        link_to_reused_ref=link_to_reused_ref,
    )

    if not os.path.exists(os.path.dirname(os.path.realpath(result_file.name))):
        raise FileNotFoundError(
            f"Output directory {os.path.dirname(os.path.realpath(result_file.name))} does not exist"
        )

    result = generate_from_schema(schema_file, config=config)

    copy_css_and_js_to_target(result_file.name, config)

    result_file.write(result)


def copy_css_and_js_to_target(result_file_path: str, config: GenerationConfiguration) -> None:
    """Copy the CSS and JS files needed to display the resulting page to the directory containing the result file"""
    files_to_copy = []
    if config.copy_css:
        files_to_copy.append(CSS_FILE_NAME)
    if config.copy_js:
        files_to_copy.append(JS_FILE_NAME)
    if not files_to_copy:
        return

    target_directory = os.path.dirname(result_file_path)
    source_directory = os.path.join(config.templates_directory, config.template_name)
    if target_directory == source_directory:
        return

    for file_to_copy in files_to_copy:
        source_file_path = os.path.join(source_directory, file_to_copy)
        if not os.path.exists(source_file_path):
            continue
        try:
            shutil.copy(source_file_path, os.path.join(target_directory, file_to_copy))
        except shutil.SameFileError:
            print(f"Not copying {file_to_copy} to {os.path.abspath(target_directory)}, file already exists")


@click.command()
@click.argument("schema_file", nargs=1, type=click.File("r", encoding="utf-8"))
@click.argument("result_file", nargs=1, type=click.File("w+", encoding="utf-8"), default="schema_doc.html")
@click.option(
    "--config-file", type=click.File("r", encoding="utf-8"), help="JSON or YAML file containing generation parameters"
)
@click.option(
    "--config",
    multiple=True,
    help="Override generation parameters from the configuration file. "
    "Format is parameter_name=parameter_value. For example: --config minify=false. Can be repeated.",
)
@click.option("--minify/--no-minify", default=True, help="Run minification on the HTML result")
@click.option(
    "--deprecated-from-description", is_flag=True, help="Look in the description to find if an attribute is deprecated"
)
@click.option(
    "--default-from-description", is_flag=True, help="Look in the description to find an attribute default value"
)
@click.option("--expand-buttons", is_flag=True, help="Add 'Expand all' and 'Collapse all' buttons at the top")
@click.option("--copy-css/--no-copy-css", default=True, help=f"Copy {CSS_FILE_NAME} to the folder of the result_file")
@click.option("--copy-js/--no-copy-js", default=True, help=f"Copy {JS_FILE_NAME} to the folder of the result_file")
@click.option(
    "--link-to-reused-ref/--no-link-to-reused-ref",
    default=True,
    help="If set and 2 parts of the schema refer to the same definition, the definition will only be rendered once "
    "and all other references will be replaced by a link.",
)
def main(
    schema_file: TextIO,
    result_file: TextIO,
    config_file: TextIO,
    config: List[str],
    minify: bool,
    deprecated_from_description: bool,
    default_from_description: bool,
    expand_buttons: bool,
    copy_css: bool,
    copy_js: bool,
    link_to_reused_ref: bool,
) -> None:
    start = datetime.now()
    config = _get_final_config(
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        copy_css=copy_css,
        copy_js=copy_js,
        link_to_reused_ref=link_to_reused_ref,
        config=config_file,
        config_parameters=config,
    )

    try:
        generate_from_file_object(schema_file, result_file, config=config)
    except FileNotFoundError as e:
        raise click.ClickException(str(e)) from e
    duration = datetime.now() - start
    print(f"Generated {result_file.name} in {duration}")


if __name__ == "__main__":
    main()
