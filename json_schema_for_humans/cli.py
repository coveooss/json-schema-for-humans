from pathlib import Path
from typing import Optional, List, Union

import click

from json_schema_for_humans.const import FileLikeType, DEFAULT_CSS_FILE_NAME, DEFAULT_JS_FILE_NAME
from json_schema_for_humans.generate import generate_schemas_doc, copy_additional_files_to_target
from json_schema_for_humans.generation_configuration import get_final_config
from json_schema_for_humans.schema.schema_importer import get_result_output, get_schemas_to_render
from json_schema_for_humans.schema.schema_to_render import SchemaToRender
from json_schema_for_humans.template_renderer import TemplateRenderer


@click.command()
@click.argument("schema_files_or_dir", nargs=1, type=click.STRING)
@click.argument("output_path_or_file", type=click.Path(writable=True, path_type=Path), required=False)
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
    "--copy-css/--no-copy-css", default=True, help=f"Copy {DEFAULT_CSS_FILE_NAME} to the folder of the result_file"
)
@click.option(
    "--copy-js/--no-copy-js", default=True, help=f"Copy {DEFAULT_JS_FILE_NAME} to the folder of the result_file"
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
    config_file: FileLikeType,
    config: List[str],
    minify: bool,
    deprecated_from_description: bool,
    default_from_description: bool,
    expand_buttons: bool,
    copy_css: bool,
    copy_js: bool,
    link_to_reused_ref: bool,
) -> None:
    config = get_final_config(
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

    schemas_to_render = get_schemas_to_render_from_cli_arguments(
        schema_files_or_dir, output_path_or_file, config.result_extension
    )

    template_renderer = TemplateRenderer(config)
    generate_schemas_doc(schemas_to_render, template_renderer)
    copy_additional_files_to_target(schemas_to_render, config)


def get_schemas_to_render_from_cli_arguments(
    schema_files_or_dir: Union[str, Path], output_path_or_file: Optional[Path], result_extension: str
) -> List[SchemaToRender]:
    schema_files_or_dir = schema_files_or_dir.split(",")
    result_output = get_result_output(output_path_or_file, schema_files_or_dir, result_extension)

    schemas_to_render: List[SchemaToRender] = []
    for schema_file_or_dir_part in schema_files_or_dir:
        schemas_to_render += get_schemas_to_render(schema_file_or_dir_part, result_output, result_extension)

    return schemas_to_render


if __name__ == "__main__":
    main()
