from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any, Union

from json_schema_for_humans.const import FileLikeType
from json_schema_for_humans.schema.intermediate_representation import build_intermediate_representation
from json_schema_for_humans.template_renderer import TemplateRenderer


class NoResultFileError(EnvironmentError):
    """Custom Exception for when there is no result file"""


@dataclass
class SchemaToRender:
    def __init__(
        self,
        schema_file: Union[Path, FileLikeType],
        result_file: Optional[Union[Path, FileLikeType]],
        output_dir: Optional[Path],
    ):
        self.schema_file = schema_file
        if isinstance(self.schema_file, Path):
            self.schema_file = self.schema_file.resolve().absolute()
        self.result_file = result_file
        if isinstance(self.result_file, Path):
            self.result_file = self.result_file.resolve().absolute()
        self.output_dir = output_dir
        if self.output_dir and isinstance(self.output_dir, Path):
            self.output_dir = self.output_dir.resolve().absolute()

    @property
    def should_write_to_disk(self) -> bool:
        return self.result_file is not None

    @property
    def schema_file_name(self) -> str:
        return self.schema_file.name

    @property
    def name_for_output(self) -> str:
        """Name of the result documentation used in log messages"""
        if self.result_file:
            return self.result_file.name
        return self.schema_file.name

    def render(self, template_renderer: TemplateRenderer, loaded_schemas: Optional[Dict[str, Any]] = None) -> str:
        """Render the schema. If a result file is defined, write to disk. Return the rendered documentation"""
        schema_file = (
            open(file=str(self.schema_file), encoding="utf-8")
            if isinstance(self.schema_file, Path)
            else self.schema_file
        )
        intermediate_schema = build_intermediate_representation(schema_file, template_renderer.config, loaded_schemas)
        rendered = template_renderer.render(intermediate_schema)

        if self.should_write_to_disk:
            self._write_to_disk(rendered)

        return rendered

    def _write_to_disk(self, rendered: str):
        if not self.result_file:
            raise NoResultFileError(
                "Attempt to write rendered schema documentation to disk, but no result file or path defined"
            )

        if isinstance(self.result_file, Path):
            with self.result_file.open("w", encoding="utf-8") as fp:
                fp.write(rendered)
        else:
            # self.result_file is file-like object
            self.result_file.write(rendered)
