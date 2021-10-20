from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any, Union, TextIO

from json_schema_for_humans.template_renderer import TemplateRenderer
from json_schema_for_humans.schema.intermediate_representation import build_intermediate_representation


@dataclass
class SchemaToRender:
    def __init__(
        self,
        schema_file: Union[Path, TextIO],
        result_file: Optional[Union[Path, TextIO]],
        output_dir: Optional[Path],
    ):
        self.schema_file = schema_file
        self.result_file = result_file
        self.output_dir = output_dir

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

    def render(self, template_renderer: TemplateRenderer, loaded_schemas: Optional[Dict[str, Any]] = None) -> str:
        schema_file = (
            open(file=str(self.schema_file), encoding="utf-8")
            if isinstance(self.schema_file, Path)
            else self.schema_file
        )
        intermediate_schema = build_intermediate_representation(schema_file, loaded_schemas)
        rendered = template_renderer.render(intermediate_schema)

        if self.should_write_to_disk:
            self._write_to_disk(rendered)

        return rendered

    def _write_to_disk(self, rendered: str):
        result_file = (
            self.result_file.open("w", encoding="utf-8") if isinstance(self.result_file, Path) else self.result_file
        )
        result_file.write(rendered)
