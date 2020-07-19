import logging
import os
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml
from _pytest.logging import LogCaptureFixture
from bs4 import BeautifulSoup

from json_schema_for_humans.generate import (
    CONFIG_DEPRECATION_MESSAGE,
    GenerationConfiguration,
    generate_from_file_object,
    generate_from_filename,
    generate_from_schema,
)
from tests.html_schema_doc_asserts import assert_basic_case
from tests.test_utils import assert_css_and_js_not_copied, get_test_case_path


def test_generate_from_schema_using_path(tmp_path: Path) -> None:
    """Test providing a schema path as a str with the file not opened"""
    rendered = generate_from_schema(get_test_case_path("basic"))

    soup = BeautifulSoup(rendered, "html.parser")

    assert_basic_case(soup)

    assert_css_and_js_not_copied(tmp_path)


def test_generate_from_schema_using_file_object(tmp_path: Path) -> None:
    """Test providing a schema path as an opened file object"""
    with open(get_test_case_path("basic")) as test_case_fp:
        rendered = generate_from_schema(test_case_fp)

    soup = BeautifulSoup(rendered, "html.parser")

    assert_basic_case(soup)

    assert_css_and_js_not_copied(tmp_path)


def test_generate_from_schema_using_path_already_loaded(tmp_path: Path) -> None:
    """Test providing a schema path as a str with the file not opened but also the loaded schema in a dict.
    Ensure the schema is not loaded again
    """
    test_case_path = os.path.realpath(get_test_case_path("basic"))

    with open(test_case_path, encoding="utf-8") as test_case_fp:
        loaded = {test_case_path: yaml.safe_load(test_case_fp.read())}

    with patch("yaml.safe_load") as patched_yaml_load:
        rendered = generate_from_schema(test_case_path, loaded_schemas=loaded)

        patched_yaml_load.assert_not_called()

    soup = BeautifulSoup(rendered, "html.parser")

    assert_basic_case(soup)

    assert_css_and_js_not_copied(tmp_path)


def test_generate_from_schema_using_file_object_already_loaded(tmp_path: Path) -> None:
    """Test providing a schema path as an opened file object but also the loaded schema in a dict.
    Ensure the schema is not loaded again
    """
    test_case_path = os.path.realpath(get_test_case_path("basic"))

    with open(test_case_path, encoding="utf-8") as test_case_fp:
        loaded = {test_case_path: yaml.safe_load(test_case_fp.read())}

    with patch("yaml.safe_load") as patched_yaml_load:
        with open(get_test_case_path("basic")) as test_case_fp:
            rendered = generate_from_schema(test_case_fp, loaded_schemas=loaded)

        patched_yaml_load.assert_not_called()

    soup = BeautifulSoup(rendered, "html.parser")

    assert_basic_case(soup)

    assert_css_and_js_not_copied(tmp_path)


def test_generate_from_file_object(tmp_path: Path) -> None:
    """Test generating from open file objects for input and output"""
    result_file_path = tmp_path / "result_with_another_name.html"

    with open(get_test_case_path("basic")) as test_case_fp:
        with result_file_path.open("w", encoding="utf-8") as result_write_fp:
            generate_from_file_object(test_case_fp, result_write_fp, False, False, False, False)

    with result_file_path.open(encoding="utf-8") as result_fp:
        soup = BeautifulSoup(result_fp.read(), "html.parser")

    assert_basic_case(soup)

    assert (tmp_path / "result_with_another_name.html").exists()

    assert (tmp_path / "schema_doc.min.js").exists()


def test_generate_from_file_name(tmp_path: Path) -> None:
    """Test generating from file names for input and output"""
    test_case_path = get_test_case_path("basic")
    result_path = tmp_path / "result_with_another_name.html"

    generate_from_filename(test_case_path, str(result_path.resolve()), False, False, False, False)

    with result_path.open(encoding="utf-8") as result_fp:
        soup = BeautifulSoup(result_fp.read(), "html.parser")

    assert (tmp_path / "result_with_another_name.html").exists()

    assert (tmp_path / "schema_doc.min.js").exists()


def _assert_deprecation_message(caplog: LogCaptureFixture, must_be_present: bool) -> None:
    log_records = [r.message for r in caplog.records]
    if must_be_present:
        assert CONFIG_DEPRECATION_MESSAGE in log_records
    else:
        assert CONFIG_DEPRECATION_MESSAGE not in log_records


@pytest.mark.parametrize("minify, expect_warning", [(True, False), (False, True)])
def test_generate_from_schema_deprecation_warning(
    tmp_path: Path, caplog: LogCaptureFixture, minify: bool, expect_warning: bool
) -> None:
    caplog.set_level(logging.INFO)

    generate_from_schema(get_test_case_path("basic"), minify=minify)

    _assert_deprecation_message(caplog, expect_warning)


@pytest.mark.parametrize("minify, expect_warning", [(True, False), (False, True)])
def test_generate_from_file_object_deprecation_warning(
    tmp_path: Path, caplog: LogCaptureFixture, minify: bool, expect_warning: bool
) -> None:
    result_file_path = tmp_path / "result_file.html"

    caplog.set_level(logging.INFO)
    with open(get_test_case_path("basic")) as test_case_fp:
        with result_file_path.open("w", encoding="utf-8") as result_write_fp:
            generate_from_file_object(test_case_fp, result_write_fp, minify=minify)

    _assert_deprecation_message(caplog, expect_warning)


@pytest.mark.parametrize("minify, expect_warning", [(True, False), (False, True)])
def test_generate_from_file_name_deprecation_warning(
    tmp_path: Path, caplog: LogCaptureFixture, minify: bool, expect_warning: bool
) -> None:
    test_case_path = get_test_case_path("basic")
    result_path = tmp_path / "result_file.html"

    caplog.set_level(logging.INFO)

    generate_from_filename(test_case_path, str(result_path.resolve()), minify=minify)

    _assert_deprecation_message(caplog, expect_warning)


def test_generate_from_schema_config_object(tmp_path: Path, caplog: LogCaptureFixture) -> None:
    config = GenerationConfiguration(minify=False, default_from_description=True, copy_css=False, copy_js=False)

    caplog.set_level(logging.INFO)

    generate_from_schema(get_test_case_path("basic"), config=config)

    _assert_deprecation_message(caplog, False)
    assert_css_and_js_not_copied(tmp_path)
