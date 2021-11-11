import os
from pathlib import Path
from typing import Optional, List, Union

import click

from json_schema_for_humans.schema.schema_to_render import SchemaToRender


def _get_schema_paths(schema_file_or_dir: Union[str, Path]) -> List[Path]:
    schema_file_paths: List[Path] = []
    if isinstance(schema_file_or_dir, str):
        schema_file_or_dir = Path(schema_file_or_dir)

    if schema_file_or_dir.is_file():
        schema_file_paths.append(schema_file_or_dir)
    elif schema_file_or_dir.is_dir():
        for glob_pattern in ["**/*.json", "**/*.yaml", "**/*.yml"]:
            schema_file_paths += [schema_path for schema_path in schema_file_or_dir.glob(glob_pattern)]
    else:
        schema_file_paths += [schema_path for schema_path in Path.cwd().glob(str(schema_file_or_dir))]

    return [p.absolute() for p in schema_file_paths]


def get_schemas_to_render(
    schema_file_or_dir: Union[str, Path],
    result_file_or_dir: Optional[Union[str, Path]],
    result_extension: str,
) -> List[SchemaToRender]:
    """Build and return a list of SchemaToRender containing the list of input schema and output file that will be
    rendered in a run
    """
    to_render: List[SchemaToRender] = []

    schema_file_paths = _get_schema_paths(schema_file_or_dir)

    if not result_file_or_dir:
        return [SchemaToRender(schema_file_path, None, None) for schema_file_path in schema_file_paths]

    # Compute output_dir where additional files will be copied if necessary
    result_path_is_dir = Path(result_file_or_dir).is_dir()
    output_dir = result_file_or_dir if result_path_is_dir else result_file_or_dir.parent
    if not output_dir.exists():
        raise FileNotFoundError(f"{output_dir} not found")

    if len(schema_file_paths) > 1 and not result_path_is_dir:
        raise AssertionError("Several schemas to render, but output path is not a directory")

    for schema_file_path in schema_file_paths:
        if result_path_is_dir:
            this_schema_result_path = (
                result_file_or_dir / f"{os.path.splitext(schema_file_path.name)[0]}.{result_extension}"
            )
        else:
            this_schema_result_path = result_file_or_dir
        to_render.append(SchemaToRender(schema_file_path, this_schema_result_path, output_dir))
    return to_render


def get_result_output(
    output_path_or_file: Optional[Path], schema_files_or_dir: List[str], result_extension: str
) -> Path:
    if not output_path_or_file:
        if len(schema_files_or_dir) > 1 or any(Path(p).is_dir() for p in schema_files_or_dir):
            output_path_or_file = Path.cwd()
        else:
            output_path_or_file = Path(f"schema_doc.{result_extension}")

    if output_path_or_file.is_dir():
        if not output_path_or_file.exists():
            raise click.ClickException(f"Output path is a directory, but it does not exist: {output_path_or_file}")
    else:
        output_directory = output_path_or_file.parent
        if not output_directory.exists():
            raise click.ClickException(f"Output path file is in a directory that does not exist: {output_directory}")
    return output_path_or_file
