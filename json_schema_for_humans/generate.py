import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, TextIO, Union

import click

from json_schema_for_humans.schema.schema_importer import import_schemas_for_creating, get_schemas_to_render
from json_schema_for_humans.schema.schema_to_render import SchemaToRender
from json_schema_for_humans.template_renderer import TemplateRenderer
from json_schema_for_humans.generation_configuration import GenerationConfiguration, _get_final_config, DefaultFile


@click.command()
@click.argument("schema_files_or_dir", nargs=1, type=click.STRING)
@click.argument(
    "output_path_or_file", type=click.Path(writable=True, path_type=Path), required=False,
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
@click.option(
    "--copy-css/--no-copy-css", default=True, help=f"Copy {DefaultFile.CSS_FILE_NAME} to the folder of the result_file"
)
@click.option(
    "--copy-js/--no-copy-js", default=True, help=f"Copy {DefaultFile.JS_FILE_NAME} to the folder of the result_file"
)
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
        link_to_reused_ref=link_to_reused_ref,
        copy_css=copy_css,
        copy_js=copy_js,
        config=config_file,
        config_parameters=config,
    )

    schemas_to_render = import_schemas_for_creating(schema_files_or_dir, output_path_or_file, config.result_extension)

    template_renderer = TemplateRenderer(config)
    _generate_schemas_doc(schemas_to_render, template_renderer)
    _copy_additional_files_to_target(schemas_to_render, template_renderer)


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
        link_to_reused_ref=link_to_reused_ref,
    )

    if isinstance(schema_file, list):
        # Backward compatibility
        schema_file = os.path.sep.join(schema_file)

    schemas_to_render = get_schemas_to_render(schema_file, None, config.result_extension)

    template_renderer = TemplateRenderer(config)
    for rendered_content in _generate_schemas_doc(schemas_to_render, template_renderer, loaded_schemas).items():
        return rendered_content[1]


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
    schemas_to_render = import_schemas_for_creating(schema_file_name, Path(result_file_name), config.template_name)
    template_renderer = TemplateRenderer(config)
    _generate_schemas_doc(schemas_to_render, template_renderer)
    _copy_additional_files_to_target(schemas_to_render, template_renderer)


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

    schemas_to_render = get_schemas_to_render(schema_file, result_file, config.result_extension)
    template_renderer = TemplateRenderer(config)
    _generate_schemas_doc(schemas_to_render, template_renderer)
    _copy_additional_files_to_target(schemas_to_render, template_renderer)


def _copy_additional_files_to_target(schemas_to_render: List[SchemaToRender], template_renderer: TemplateRenderer):
    for output_directory in set(
        schema_to_render.output_dir for schema_to_render in schemas_to_render if schema_to_render.output_dir
    ):
        for file_to_copy in template_renderer.files_to_copy():
            _copy_additional_file_to_target(
                file_to_copy,
                output_directory,
                template_renderer.template_directory(),
                template_renderer.template_name(),
            )


def _copy_additional_file_to_target(
    file_to_copy: DefaultFile, target_directory: Path, templates_directory: str, template_name: str
) -> None:
    """Copy the file needed to display the resulting page to the directory containing the result file"""

    source_directory = Path(templates_directory) / template_name
    if not target_directory or target_directory == source_directory:
        return

    source_file_path = source_directory / file_to_copy.value
    if not source_file_path.exists():
        return

    try:
        shutil.copy(str(source_file_path), str(target_directory / file_to_copy.value))
    except shutil.SameFileError:
        print(f"Not copying {file_to_copy} to {target_directory.absolute()}, file already exists")


def _generate_schema(
    schema_to_render: SchemaToRender, template_renderer: TemplateRenderer, loaded_schemas: Optional[Dict[str, Any]]
) -> str:
    start = datetime.now()
    print(f"== Generating {schema_to_render.name_for_output} ==")
    result = schema_to_render.render(template_renderer, loaded_schemas)
    print(f"== Generated {schema_to_render.name_for_output} in {datetime.now() - start} ==")

    return result


def _generate_schemas_doc(
    schemas_to_render: List[SchemaToRender],
    template_renderer: TemplateRenderer,
    loaded_schemas: Optional[Dict[str, Any]] = None,
) -> Dict[str, str]:
    """Generate documentation from one or more schemas and either write to disk or return the rendered content"""
    rendered_schemas: Dict[str, str] = {}

    for schema_to_render in schemas_to_render:
        rendered_schemas[schema_to_render.schema_file_name] = _generate_schema(
            schema_to_render, template_renderer, loaded_schemas
        )

    return rendered_schemas


if __name__ == "__main__":
    main()
