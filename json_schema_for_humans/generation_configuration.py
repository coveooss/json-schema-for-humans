import json
import logging
import os
from dataclasses import dataclass
from json import JSONDecodeError
from pathlib import Path
from typing import Any, Union, Dict, List, Optional

import yaml
from dataclasses_json import dataclass_json

from json_schema_for_humans.const import (
    DocumentationTemplate,
    FileLikeType,
    DEFAULT_CSS_FILE_NAME,
    DEFAULT_JS_FILE_NAME,
)


@dataclass_json
@dataclass
class GenerationConfiguration:
    """Configuration for generating documentation for a schema"""

    minify: bool = True
    description_is_markdown: bool = True
    deprecated_from_description: bool = False
    show_breadcrumbs: bool = True
    collapse_long_descriptions: bool = True
    default_from_description: bool = False
    expand_buttons: bool = False
    copy_css: bool = True
    copy_js: bool = True
    link_to_reused_ref: bool = True
    recursive_detection_depth: int = 25
    templates_directory: Union[str, Path] = Path(__file__).parent / "templates"
    template_name: str = "js"
    custom_template_path: Optional[str] = None
    show_toc: bool = True
    examples_as_yaml: bool = False
    # markdown2 extra parameters can be added here: https://github.com/trentm/python-markdown2/wiki/Extras
    markdown_options: Optional[Dict[str, Any]] = None
    template_md_options: Optional[Dict[str, Any]] = None
    with_footer: bool = True
    footer_show_time: bool = True

    def __post_init__(self) -> None:
        default_markdown_options = {
            "break-on-newline": True,
            "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
            "tables": None,
        }
        default_markdown_options.update(self.markdown_options or {})
        self.markdown_options = default_markdown_options

        default_template_md_options = {
            "badge_as_image": False,
            "show_heading_numbers": True,
            "show_array_restrictions": True,
        }
        default_template_md_options.update(self.template_md_options or {})
        self.template_md_options = default_template_md_options

    @property
    def templates_directory_path(self) -> Path:
        return Path(self.templates_directory)

    @property
    def files_to_copy(self) -> List[str]:
        files_to_copy: List[str] = []
        if self.copy_js:
            files_to_copy.append(DEFAULT_JS_FILE_NAME)
        if self.copy_css:
            files_to_copy.append(DEFAULT_CSS_FILE_NAME)
        return files_to_copy

    @property
    def template_is_markdown(self) -> bool:
        return self.result_extension == "md"

    @property
    def template_is_html(self) -> bool:
        return self.result_extension == "html"

    @property
    def result_extension(self) -> str:
        """File extension for the resulting documentation"""
        if self.custom_template_path:
            return Path(self.custom_template_path).suffix[1:]

        if self.template_name:
            return DocumentationTemplate(self.template_name).result_extension

        raise ValueError("Trying to get extension for configuration with no template")

    @property
    def template_path(self) -> Optional[Path]:
        if self.custom_template_path:
            return Path(self.custom_template_path)

        return (
            Path(__file__).parent
            / "templates"
            / self.template_name
            / f"base.{DocumentationTemplate(self.template_name).result_extension}"
        )


CONFIG_DEPRECATION_MESSAGE = (
    "JSON Schema for humans: Please supply a GenerationConfiguration object instead of individual options"
)


def get_final_config(
    minify: bool,
    deprecated_from_description: bool,
    default_from_description: bool,
    expand_buttons: bool,
    link_to_reused_ref: bool,
    copy_css: bool = False,
    copy_js: bool = False,
    config: Optional[Union[str, Path, FileLikeType, Dict[str, Any], GenerationConfiguration]] = None,
    config_parameters: List[str] = None,
) -> GenerationConfiguration:
    if config:
        final_config = _load_config(config)
    else:
        final_config = GenerationConfiguration(
            minify=minify,
            deprecated_from_description=deprecated_from_description,
            default_from_description=default_from_description,
            expand_buttons=expand_buttons,
            link_to_reused_ref=link_to_reused_ref,
            copy_css=copy_css,
            copy_js=copy_js,
        )
        if (
            not minify
            or deprecated_from_description
            or default_from_description
            or expand_buttons
            or not link_to_reused_ref
        ):
            logging.info(CONFIG_DEPRECATION_MESSAGE)

    if config_parameters:
        final_config = _apply_config_cli_parameters(final_config, config_parameters)

    return final_config


def _load_config(
    config_parameter: Union[str, Path, FileLikeType, Dict[str, Any], GenerationConfiguration]
) -> GenerationConfiguration:
    """Load the configuration from either the path (as str or Path) to a config file, the open config file object,
    The loaded config as a dict or the GenerateConfiguration object directly.
    """
    if isinstance(config_parameter, GenerationConfiguration):
        return config_parameter

    if isinstance(config_parameter, dict):
        config_dict = config_parameter
    elif isinstance(config_parameter, (str, Path)):
        if isinstance(config_parameter, str):
            real_path = os.path.realpath(config_parameter)
        else:
            real_path = str(config_parameter.resolve())
        with open(os.path.realpath(real_path), encoding="utf-8") as config_fp:
            config_dict = yaml.safe_load(config_fp.read())
    else:
        config_dict = yaml.safe_load(config_parameter.read())

    return GenerationConfiguration.from_dict(config_dict)  # type: ignore


def _apply_config_cli_parameters(
    current_configuration: GenerationConfiguration, config_cli_parameters: List[str]
) -> GenerationConfiguration:
    current_configuration_as_dict = current_configuration.to_dict()  # type: ignore
    parameter_value: Union[str, bool, int]
    for parameter in config_cli_parameters:
        if "=" in parameter:
            parameter_name, parameter_value = parameter.split("=")
            try:
                parameter_value = json.loads(parameter_value)
            except JSONDecodeError:
                pass
        else:
            parameter_name = parameter
            if parameter_name.startswith("no_") or parameter_name.startswith("no-"):
                parameter_value = False
                parameter_name = parameter_name[3:]  # Strip the `no_`/`no-`
            else:
                parameter_value = True
        current_configuration_as_dict[parameter_name] = parameter_value

    return GenerationConfiguration.from_dict(current_configuration_as_dict)  # type: ignore
