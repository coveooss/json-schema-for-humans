import os
from pathlib import Path
from typing import Optional

from bs4 import BeautifulSoup

from json_schema_for_humans.const import DEFAULT_CSS_FILE_NAME, DEFAULT_JS_FILE_NAME
from json_schema_for_humans.generate import generate_from_schema
from json_schema_for_humans.generation_configuration import GenerationConfiguration

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)


def assert_css_and_js_not_copied(path: Path) -> None:
    """Assert that the standard CCS and JS files were not copied over"""
    assert not (path / DEFAULT_CSS_FILE_NAME).exists()

    assert not (path / DEFAULT_JS_FILE_NAME).exists()


def assert_css_and_js_copied(path: Path) -> None:
    """Assert that the standard CCS and JS files were copied over"""
    assert (path / DEFAULT_CSS_FILE_NAME).exists()

    assert (path / DEFAULT_JS_FILE_NAME).exists()


def get_test_cases_path() -> str:
    return os.path.realpath(os.path.join(parent_dir, "docs", "examples", "cases"))


def get_test_case_path(name: str) -> str:
    """Get the loaded JSON schema for a test case"""
    return os.path.realpath(os.path.join(get_test_cases_path(), f"{name}.json"))


def get_nonexistent_output_path(name: str) -> str:
    """Get the location of a non-existent output file"""
    return os.path.realpath(os.path.join(parent_dir, "not", "a", "path", f"{name}.html"))


def generate_case(case_name: str, config: Optional[GenerationConfiguration] = None) -> BeautifulSoup:
    """Get the BeautifulSoup object for a test case"""
    return BeautifulSoup(
        generate_from_schema(get_test_case_path(case_name), None, config=config),
        "html.parser",
    )
