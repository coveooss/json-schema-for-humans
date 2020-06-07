import os
from pathlib import Path
from unittest.mock import patch

import yaml
from bs4 import BeautifulSoup

from json_schema_for_humans.generate import generate_from_file_object, generate_from_filename, generate_from_schema
from tests.generate_test import _assert_basic_case
from tests.test_utils import _get_test_case_path


def _assert_css_and_js_not_copied(path: Path) -> None:
    """Assert that the standard CCS and JS files were not copied over"""
    assert not (path / "schema_doc.html").exists()

    assert not (path / "schema_doc.min.js").exists()


def test_generate_from_schema_using_path(tmp_path: Path) -> None:
    """Test providing a schema path as a str with the file not opened"""
    rendered = generate_from_schema(_get_test_case_path("basic"))

    soup = BeautifulSoup(rendered, "html.parser")

    _assert_basic_case(soup)

    _assert_css_and_js_not_copied(tmp_path)


def test_generate_from_schema_using_file_object(tmp_path: Path) -> None:
    """Test providing a schema path as an opened file object"""
    with open(_get_test_case_path("basic")) as test_case_fp:
        rendered = generate_from_schema(test_case_fp)

    soup = BeautifulSoup(rendered, "html.parser")

    _assert_basic_case(soup)

    _assert_css_and_js_not_copied(tmp_path)


def test_generate_from_schema_using_path_already_loaded(tmp_path: Path) -> None:
    """Test providing a schema path as a str with the file not opened but also the loaded schema in a dict.
    Ensure the schema is not loaded again
    """
    test_case_path = os.path.realpath(_get_test_case_path("basic"))

    with open(test_case_path, encoding="utf-8") as test_case_fp:
        loaded = {test_case_path: yaml.safe_load(test_case_fp.read())}

    with patch("yaml.safe_load") as patched_yaml_load:
        rendered = generate_from_schema(test_case_path, loaded_schemas=loaded)

        patched_yaml_load.assert_not_called()

    soup = BeautifulSoup(rendered, "html.parser")

    _assert_basic_case(soup)

    _assert_css_and_js_not_copied(tmp_path)


def test_generate_from_schema_using_file_object_already_loaded(tmp_path: Path) -> None:
    """Test providing a schema path as an opened file object but also the loaded schema in a dict.
    Ensure the schema is not loaded again
    """
    test_case_path = os.path.realpath(_get_test_case_path("basic"))

    with open(test_case_path, encoding="utf-8") as test_case_fp:
        loaded = {test_case_path: yaml.safe_load(test_case_fp.read())}

    with patch("yaml.safe_load") as patched_yaml_load:
        with open(_get_test_case_path("basic")) as test_case_fp:
            rendered = generate_from_schema(test_case_fp, loaded_schemas=loaded)

        patched_yaml_load.assert_not_called()

    soup = BeautifulSoup(rendered, "html.parser")

    _assert_basic_case(soup)

    _assert_css_and_js_not_copied(tmp_path)


def test_generate_from_file_object(tmp_path: Path) -> None:
    """Test generating from open file objects for input and output"""
    result_file_path = tmp_path / "result_with_another_name.html"

    with open(_get_test_case_path("basic")) as test_case_fp:
        with result_file_path.open("w", encoding="utf-8") as result_write_fp:
            generate_from_file_object(test_case_fp, result_write_fp, False, False, False, False)

    with result_file_path.open(encoding="utf-8") as result_fp:
        soup = BeautifulSoup(result_fp.read(), "html.parser")

    _assert_basic_case(soup)

    assert (tmp_path / "result_with_another_name.html").exists()

    assert (tmp_path / "schema_doc.min.js").exists()


def test_generate_from_file_name(tmp_path: Path) -> None:
    """Test generating from file names for input and output"""
    test_case_path = _get_test_case_path("basic")
    result_path = tmp_path / "result_with_another_name.html"

    generate_from_filename(test_case_path, str(result_path.resolve()), False, False, False, False)

    with result_path.open(encoding="utf-8") as result_fp:
        soup = BeautifulSoup(result_fp.read(), "html.parser")

    assert (tmp_path / "result_with_another_name.html").exists()

    assert (tmp_path / "schema_doc.min.js").exists()
