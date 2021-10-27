import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from json_schema_for_humans.const import FileLikeType
from json_schema_for_humans.generation_configuration import GenerationConfiguration, get_final_config
from json_schema_for_humans.schema.schema_importer import get_schemas_to_render
from json_schema_for_humans.schema.schema_to_render import SchemaToRender
from json_schema_for_humans.template_renderer import TemplateRenderer


def generate_from_schema(
    schema_file: Union[str, Path],
    loaded_schemas: Optional[Dict[str, Any]] = None,
    minify: bool = True,
    deprecated_from_description: bool = False,
    default_from_description: bool = False,
    expand_buttons: bool = False,
    link_to_reused_ref: bool = True,
    config: GenerationConfiguration = None,
) -> str:
    config = config or get_final_config(
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        link_to_reused_ref=link_to_reused_ref,
    )

    schemas_to_render = get_schemas_to_render(schema_file, None, config.result_extension)

    template_renderer = TemplateRenderer(config)
    for rendered_content in generate_schemas_doc(schemas_to_render, template_renderer, loaded_schemas).items():
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
    config = config or get_final_config(
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        copy_css=copy_css,
        copy_js=copy_js,
        link_to_reused_ref=link_to_reused_ref,
    )

    schemas_to_render = get_schemas_to_render(schema_file_name, Path(result_file_name), config.result_extension)

    template_renderer = TemplateRenderer(config)
    generate_schemas_doc(schemas_to_render, template_renderer)
    copy_additional_files_to_target(schemas_to_render, config)


def generate_from_file_object(
    schema_file: FileLikeType,
    result_file: FileLikeType,
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
    config = config or get_final_config(
        minify=minify,
        deprecated_from_description=deprecated_from_description,
        default_from_description=default_from_description,
        expand_buttons=expand_buttons,
        copy_css=copy_css,
        copy_js=copy_js,
        link_to_reused_ref=link_to_reused_ref,
    )

    schemas_to_render = [SchemaToRender(schema_file, result_file, Path(result_file.name).parent)]
    template_renderer = TemplateRenderer(config)
    generate_schemas_doc(schemas_to_render, template_renderer)
    copy_additional_files_to_target(schemas_to_render, config)


def copy_additional_files_to_target(schemas_to_render: List[SchemaToRender], config: GenerationConfiguration):
    for output_directory in set(
        schema_to_render.output_dir for schema_to_render in schemas_to_render if schema_to_render.output_dir
    ):
        for file_to_copy in config.files_to_copy:
            _copy_additional_file_to_target(
                file_to_copy,
                config.template_path.parent,
                output_directory,
            )


def _copy_additional_file_to_target(
    file_to_copy: str,
    source_directory: Path,
    target_directory: Path,
) -> None:
    """Copy the file needed to display the resulting page to the directory containing the result file"""

    if target_directory == source_directory:
        return

    source_file_path = source_directory / file_to_copy
    if not source_file_path.exists():
        return

    try:
        shutil.copy(str(source_file_path), str(target_directory / file_to_copy))
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


def generate_schemas_doc(
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
