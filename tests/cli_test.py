import os
import traceback
from pathlib import Path

from bs4 import BeautifulSoup
from click.testing import CliRunner, Result

from json_schema_for_humans.cli import main
from tests.test_utils import (
    assert_css_and_js_copied,
    assert_css_and_js_not_copied,
    get_nonexistent_output_path,
    get_test_case_path,
)


def assert_cli_runner_result(result: Result) -> None:
    """Assert that the exit code of a CliRunner run is 0. If it isn't, print the exception info before"""
    if not result.exit_code == 0:
        print(result.exception)
        if result.exc_info:
            if len(result.exc_info) >= 3:
                traceback.print_tb(result.exc_info[2])
            else:
                print(result.exc_info)
    assert result.exit_code == 0


def assert_cli_runner_exited(result: Result, expected_exception_text: str) -> None:
    assert result.exit_code > 0
    assert expected_exception_text in result.stdout


def test_generate_using_cli_default() -> None:
    """Test the standard case of generating using the CLI"""
    test_path = get_test_case_path("basic")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [test_path])
        assert_cli_runner_result(result)

        assert Path("schema_doc.html").exists()

        assert_css_and_js_copied(Path.cwd())


def test_generate_using_cli_default_result_file() -> None:
    """Test providing a different result file path to the CLI"""
    test_path = get_test_case_path("basic")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [test_path, "doc.html"])
        assert_cli_runner_result(result)

        assert Path("doc.html").exists()

        assert_css_and_js_copied(Path.cwd())


def test_generate_using_cli_multiple(tmp_path: Path) -> None:
    """Test providing several schemas to render using the CLI"""
    test_case1 = "basic"
    test_path1 = get_test_case_path(test_case1)
    test_case2 = "with_default"
    test_path2 = get_test_case_path(test_case2)

    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [f"{test_path1},{test_path2}", str(tmp_path)])
        assert_cli_runner_result(result)

        assert (tmp_path / f"{test_case1}.html").exists()
        assert (tmp_path / f"{test_case2}.html").exists()

        assert_css_and_js_copied(tmp_path)


def test_cli_output_default_html() -> None:
    """Test the default value for the output path for a single HTML schema"""
    test_path = get_test_case_path("basic")

    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [str(test_path)])
        assert_cli_runner_result(result)

        assert Path("schema_doc.html").exists()


def test_cli_output_default_md() -> None:
    """Test the default value for the output path for a single MD schema"""
    test_path = get_test_case_path("basic")

    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [str(test_path), "--config", "template_name=md"])
        assert_cli_runner_result(result)

        assert Path("schema_doc.md").exists()


def test_cli_output_default_cwd() -> None:
    """Test the default value for the output path for several schemas"""
    test_case1 = "basic"
    test_path1 = get_test_case_path(test_case1)
    test_case2 = "with_default"
    test_path2 = get_test_case_path(test_case2)

    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [f"{test_path1},{test_path2}"])
        assert_cli_runner_result(result)

        assert Path(f"{test_case1}.html").exists()
        assert Path(f"{test_case2}.html").exists()

        assert_css_and_js_copied(Path.cwd())


def test_config_parameters() -> None:
    """Test providing configuration parameters using the --config CLI parameter"""
    test_path = get_test_case_path("basic")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [test_path, "--config", "copy_css=false", "--config", "copy_js=false"])
        assert_cli_runner_result(result)

        assert_css_and_js_not_copied(Path.cwd())


def test_config_parameters_with_nonexistent_output_path() -> None:
    """Test providing a non-existent output path fails with informative error message"""
    test_path = get_test_case_path("basic")
    output_dir = get_nonexistent_output_path("schema")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [test_path, output_dir, "--config", "copy_css=false", "--config", "copy_js=false"])
        assert_cli_runner_exited(
            result, f"Output path file is in a directory that does not exist: {os.path.dirname(output_dir)}"
        )


def test_nonexistent_output_path() -> None:
    """Test providing a non-existent output path fails with informative error message"""
    test_path = get_test_case_path("basic")
    output_dir = get_nonexistent_output_path("schema")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [test_path, output_dir])
        assert_cli_runner_exited(
            result,
            f"Output path file is in a directory that does not exist: {os.path.dirname(output_dir)}",
        )


def test_config_parameters_flags_yes() -> None:
    """Test providing configuration parameters using the --config CLI parameter and the special syntax for flags"""
    test_path = get_test_case_path("basic")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [test_path, "--config", "expand_buttons"])
        assert_cli_runner_result(result)

        assert_css_and_js_copied(Path.cwd())
        assert Path("schema_doc.html").exists()

        with open("schema_doc.html", "r", encoding="utf-8") as schema_doc:
            soup = BeautifulSoup(schema_doc.read(), "html.parser")
            expand_button = soup.find("button", text="Expand all")
            assert expand_button


def test_config_parameters_flags_no() -> None:
    """Test providing configuration parameters using the --config CLI parameter and the special 'no_' syntax for flags"""
    test_path = get_test_case_path("basic")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, [test_path, "--config", "no_copy_css", "--config", "no_copy_js"])
        assert_cli_runner_result(result)

        assert_css_and_js_not_copied(Path.cwd())


def test_config_file_parameter_json() -> None:
    test_path = get_test_case_path("basic")
    runner = CliRunner()
    with runner.isolated_filesystem():
        config_file_name = "jsfh_config.json"
        with open(config_file_name, "w", encoding="utf-8") as config_file:
            config_file.write("""{"copy_css": false, "copy_js": false}""")

        result = runner.invoke(main, [test_path, "--config-file", config_file_name])
        assert_cli_runner_result(result)

        assert_css_and_js_not_copied(Path.cwd())


def test_config_file_parameter_yaml() -> None:
    test_path = get_test_case_path("basic")
    runner = CliRunner()
    with runner.isolated_filesystem():
        config_file_name = "jsfh_config.yaml"
        with open(config_file_name, "w", encoding="utf-8") as config_file:
            config_file.write("""copy_css: false\ncopy_js: false""")

        result = runner.invoke(main, [test_path, "--config-file", config_file_name])
        assert_cli_runner_result(result)

        assert_css_and_js_not_copied(Path.cwd())
