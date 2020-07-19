import os
from pathlib import Path

from bs4 import BeautifulSoup

from json_schema_for_humans.generate import generate_from_schema


def assert_css_and_js_not_copied(path: Path) -> None:
    """Assert that the standard CCS and JS files were not copied over"""
    assert not (path / "schema_doc.css").exists()

    assert not (path / "schema_doc.min.js").exists()


def assert_css_and_js_copied(
    path: Path, css_file_name: str = "schema_doc.css", js_file_name: str = "schema_doc.min.js"
) -> None:
    """Assert that the standard CCS and JS files were copied over"""
    assert (path / css_file_name).exists()

    assert (path / js_file_name).exists()


def get_test_case_path(name: str) -> str:
    """Get the loaded JSON schema for a test case"""
    return os.path.realpath(os.path.join(os.path.dirname(__file__), "cases", f"{name}.json"))


def generate_case(
    case_name: str, find_deprecated: bool = False, find_default: bool = False, link_to_reused_ref: bool = True
) -> BeautifulSoup:
    """Get the BeautifulSoup object for a test case"""
    return BeautifulSoup(
        generate_from_schema(
            get_test_case_path(case_name),
            None,
            False,
            find_deprecated,
            find_default,
            True,
            link_to_reused_ref=link_to_reused_ref,
        ),
        "html.parser",
    )
