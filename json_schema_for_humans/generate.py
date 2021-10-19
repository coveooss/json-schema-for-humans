import os
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, TextIO, Tuple, Union

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


@dataclass
class SchemaToRender:
    schema_file: Union[Path, TextIO]
    result_file: Optional[Union[Path, TextIO]]
    output_dir: Optional[Path]

    config: GenerationConfiguration

    @property
    def should_write_to_disk(self) -> bool:
        return self.result_file is not None

    @property
    def schema_file_name(self) -> str:
        return self.schema_file.name

    @property
    def name_for_output(self) -> str:
        if self.result_file:
            return self.result_file.name
        return self.schema_file.name

    def render(self, template: "Template", loaded_schemas: Optional[Dict[str, Any]] = None) -> str:
        if isinstance(self.schema_file, Path):
            with open(self.schema_file, encoding="utf-8") as schema_file:
                intermediate_schema = build_intermediate_representation(schema_file, self.config, loaded_schemas)
        else:
            intermediate_schema = build_intermediate_representation(self.schema_file, self.config, loaded_schemas)

        rendered = template.render(schema=intermediate_schema, config=self.config)

        if self.config.minify:
            if self.config.is_markdown_template:
                # remove multiple contiguous empty lines
                rendered = re.sub(r"\n\s*\n", "\n\n", rendered)
            else:
                rendered = htmlmin.minify(rendered)

        return rendered

    def write_to_disk(self, template: "Template", loaded_schemas: Optional[Dict[str, Any]] = None) -> Path:
        assert self.result_file is not None

        rendered = self.render(template, loaded_schemas)

        if isinstance(self.result_file, Path):
            with self.result_file.open("w", encoding="utf-8") as result_file:
                result_file.write(rendered)
                result_file_path = Path(result_file.name)
        else:
            self.result_file.write(rendered)
            result_file_path = self.result_file

        return result_file_path


def _get_schema_paths(schema_file_or_dir: Union[str, Path]) -> List[Path]:
    schema_file_paths: List[Path] = []
    if isinstance(schema_file_or_dir, str):
        schema_file_or_dir = Path(schema_file_or_dir)
    if not isinstance(schema_file_or_dir, Path):
        raise AssertionError("_get_schema_paths called with schema_file_or_dir not being a str or Path object")

    if schema_file_or_dir.is_file():
        schema_file_paths.append(schema_file_or_dir)
    else:
        schema_file_paths += [schema_path for schema_path in schema_file_or_dir.glob("**/*.json")]
        schema_file_paths += [schema_path for schema_path in schema_file_or_dir.glob("**/*.ya?ml")]

    return schema_file_paths


def _get_jinja_template(config: GenerationConfiguration = None) -> "Template":
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

    return template


def _copy_css_and_js_to_target(target_directory: Path, config: GenerationConfiguration) -> None:
    """Copy the CSS and JS files needed to display the resulting page to the directory containing the result file"""
    files_to_copy = []
    if config.copy_css:
        files_to_copy.append(CSS_FILE_NAME)
    if config.copy_js:
        files_to_copy.append(JS_FILE_NAME)
    if not files_to_copy:
        return

    source_directory = Path(config.templates_directory) / config.template_name
    if target_directory == source_directory:
        return

    for file_to_copy in files_to_copy:
        source_file_path = source_directory / file_to_copy
        if not source_file_path.exists():
            continue
        try:
            shutil.copy(str(source_file_path), str(target_directory / file_to_copy))
        except shutil.SameFileError:
            print(f"Not copying {file_to_copy} to {target_directory.absolute()}, file already exists")


def _get_schemas_to_render(
    schema_file_or_dir: Union[str, Path, TextIO],
    result_file_or_dir: Optional[Union[str, Path, TextIO]],
    config: GenerationConfiguration,
) -> List[SchemaToRender]:
    to_render: List[SchemaToRender] = []

    if isinstance(schema_file_or_dir, (str, Path)):
        schema_file_paths = _get_schema_paths(schema_file_or_dir)
    else:
        schema_file_paths = [schema_file_or_dir]

    if result_file_or_dir:
        if not isinstance(result_file_or_dir, (str, Path)):
            result_path = result_file_or_dir
            output_dir = Path(result_file_or_dir.name).parent
            result_path_is_dir = False
        else:
            result_path = Path(result_file_or_dir)
            result_path_is_dir = result_path.is_dir()
            if result_path_is_dir:
                output_dir = result_path
            else:
                output_dir = result_path.parent
        if not output_dir.exists():
            raise FileNotFoundError(f"{output_dir} not found")

        if len(schema_file_paths) > 1 and not result_path_is_dir:
            raise AssertionError("Several schemas to render, but output path is not a directory")

        for schema_file_path in schema_file_paths:
            if result_path_is_dir:
                assert result_path is not None
                result_path_or_pointer = (
                    Path(result_path) / f"{os.path.splitext(schema_file_path.name)[0]}.{config.result_extension}"
                )
            else:
                result_path_or_pointer = result_path
            to_render.append(SchemaToRender(schema_file_path, result_path_or_pointer, output_dir, config))
        return to_render
    else:
        return [SchemaToRender(schema_file_path, None, None, config) for schema_file_path in schema_file_paths]


def generate(
    schema_file_or_dir: List[Union[str, Path, TextIO]],
    result_file_or_dir: Optional[Union[str, Path, TextIO]],
    config: GenerationConfiguration = None,
    loaded_schemas: Optional[Dict[str, Any]] = None,
) -> Tuple[List[Path], Dict[str, str]]:
    """Generate documentation from one or more schemas and either write to disk or return the rendered content"""
    config = config or GenerationConfiguration()

    template = _get_jinja_template(config)

    all_to_render: List[SchemaToRender] = []
    for schema_file_or_dir_part in schema_file_or_dir:
        all_to_render += _get_schemas_to_render(schema_file_or_dir_part, result_file_or_dir, config)

    result_paths: List[Path] = []
    rendered_schemas: Dict[str, str] = {}
    for schema_to_render in all_to_render:
        start = datetime.now()
        print(f"== Generating {schema_to_render.name_for_output} ==")

        if schema_to_render.should_write_to_disk:
            result_paths.append(schema_to_render.write_to_disk(template, loaded_schemas))
        else:
            rendered_schemas[schema_to_render.schema_file_name] = schema_to_render.render(template, loaded_schemas)

        print(f"== Generated {schema_to_render.name_for_output} in {datetime.now() - start} ==")

    for output_directory in set(
        schema_to_render.output_dir for schema_to_render in all_to_render if schema_to_render.output_dir
    ):
        _copy_css_and_js_to_target(output_directory, config)

    return result_paths, rendered_schemas


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

    if isinstance(schema_file, list):
        # Backward compatibility
        schema_file = os.path.sep.join(schema_file)

    for rendered_name, rendered_content in generate([schema_file], None, config, loaded_schemas)[1].items():
        return rendered_content


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

    generate([schema_file_name], result_file_name, config=config)


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

    generate([schema_file], result_file, config)


@click.command()
@click.argument("schema_files_or_dir", nargs=1, type=click.STRING)
@click.argument(
    "output_path_or_file",
    type=click.Path(writable=True, path_type=Path),
    required=False,
)
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
    schema_files_or_dir: str,
    output_path_or_file: Optional[Path],
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

    schema_files_or_dir = schema_files_or_dir.split(",")

    if not output_path_or_file:
        if len(schema_files_or_dir) > 1 or any(Path(p).is_dir() for p in schema_files_or_dir):
            output_path_or_file = Path.cwd()
        else:
            output_path_or_file = Path(f"schema_doc.{config.result_extension}")

    if output_path_or_file.is_dir():
        if not output_path_or_file.exists():
            raise click.ClickException(f"Output path is a directory, but it does not exist: {output_path_or_file}")
    else:
        output_directory = output_path_or_file.parent
        if not output_directory.exists():
            raise click.ClickException(f"Output path file is in a directory that does not exist: {output_directory}")

    generate(schema_files_or_dir, output_path_or_file, config=config)


if __name__ == "__main__":
    main()
