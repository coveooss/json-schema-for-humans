from pathlib import Path
from typing import Optional, List, Union, TextIO

import click
import os

from json_schema_for_humans.schema.schema_to_render import SchemaToRender
from json_schema_for_humans.generation_configuration import LanguageTypes


def _get_schema_paths(schema_file_or_dir: Union[str, Path]) -> List[Path]:
    schema_file_paths: List[Path] = []
    if isinstance(schema_file_or_dir, str):
        schema_file_or_dir = Path(schema_file_or_dir)

    if schema_file_or_dir.is_file():
        schema_file_paths.append(schema_file_or_dir)
    else:
        schema_file_paths += [schema_path for schema_path in schema_file_or_dir.glob("**/*.json")]
        schema_file_paths += [schema_path for schema_path in schema_file_or_dir.glob("**/*.ya?ml")]

    return schema_file_paths


def get_schemas_to_render(
    schema_file_or_dir: Union[str, Path, TextIO],
    result_file_or_dir: Optional[Union[str, Path]],
    result_extension: LanguageTypes,
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
                    Path(result_path) / f"{os.path.splitext(schema_file_path.name)[0]}.{result_extension.value}"
                )
            else:
                result_path_or_pointer = result_path
            to_render.append(SchemaToRender(schema_file_path, result_path_or_pointer, output_dir))
        return to_render
    else:
        return [SchemaToRender(schema_file_path, None, None) for schema_file_path in schema_file_paths]


def _get_result_output(
    output_path_or_file: Optional[Path], schema_files_or_dir: List[str], result_extension: LanguageTypes
) -> Path:
    if not output_path_or_file:
        if len(schema_files_or_dir) > 1 or any(Path(p).is_dir() for p in schema_files_or_dir):
            output_path_or_file = Path.cwd()
        else:
            output_path_or_file = Path(f"schema_doc.{result_extension.value}")

    if output_path_or_file.is_dir():
        if not output_path_or_file.exists():
            raise click.ClickException(f"Output path is a directory, but it does not exist: {output_path_or_file}")
    else:
        output_directory = output_path_or_file.parent
        if not output_directory.exists():
            raise click.ClickException(f"Output path file is in a directory that does not exist: {output_directory}")
    return output_path_or_file


def import_schemas_for_creating(
    schema_files_or_dir: Union[str, Path], output_path_or_file: Optional[Path], result_extension: LanguageTypes
) -> List[SchemaToRender]:
    schema_files_or_dir = schema_files_or_dir.split(",")
    output = _get_result_output(output_path_or_file, schema_files_or_dir, result_extension)

    schemas_to_render: List[SchemaToRender] = []
    for schema_file_or_dir_part in schema_files_or_dir:
        schemas_to_render += get_schemas_to_render(schema_file_or_dir_part, output, result_extension)

    return schemas_to_render
