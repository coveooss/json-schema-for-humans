from dataclasses import dataclass
from pathlib import Path
from typing import Union, Dict, Any, List, Tuple

import pytest
from _pytest.monkeypatch import MonkeyPatch

from json_schema_for_humans.schema.schema_importer import _get_schema_paths


@dataclass
class FileTree:
    directories: List[Tuple[str, "FileTree"]]
    files: List[str]


@dataclass
class GetSchemaPathsTestCase:
    name: str
    file_tree: FileTree
    input_path: str
    expected_schema_paths: List[str]

    def __str__(self) -> str:
        return self.name


def create_file_tree(tmpdir: Path, desired_tree: FileTree) -> None:
    def _create_file_tree(current_path: Path, current_desired_tree: FileTree) -> None:
        for desired_directory_name, desired_directory_tree in current_desired_tree.directories:
            new_dir = current_path / desired_directory_name
            new_dir.mkdir()
            _create_file_tree(new_dir, desired_directory_tree)
        for desired_file in current_desired_tree.files:
            (current_path / desired_file).write_text('{"test": "value"}', encoding="utf-8")

    _create_file_tree(tmpdir, desired_tree)


@pytest.mark.parametrize("is_path", [True, False])
@pytest.mark.parametrize(
    "case",
    [
        GetSchemaPathsTestCase(
            name="file",
            file_tree=FileTree(directories=[], files=["test_schema.json"]),
            input_path="test_schema.json",
            expected_schema_paths=["test_schema.json"],
        ),
        GetSchemaPathsTestCase(
            name="dir",
            file_tree=FileTree(
                directories=[("testdir", FileTree(directories=[], files=["a.json", "b.yaml", "c.yml", "d.notyaml"]))],
                files=[],
            ),
            input_path="testdir",
            expected_schema_paths=["testdir/a.json", "testdir/b.yaml", "testdir/c.yml"],
        ),
        GetSchemaPathsTestCase(
            name="glob",
            file_tree=FileTree(
                directories=[
                    (
                        "testdir",
                        FileTree(directories=[], files=["a.json", "b.yaml", "c.yml", "d.notyaml", "e.yaml.template"]),
                    )
                ],
                files=[],
            ),
            input_path="testdir/*.yaml.*",
            expected_schema_paths=["testdir/e.yaml.template"],
        ),
    ],
    ids=str,
)
def test_get_schema_paths(is_path: bool, case: GetSchemaPathsTestCase, tmpdir: Path, monkeypatch: MonkeyPatch) -> None:
    create_file_tree(tmpdir, case.file_tree)

    monkeypatch.chdir(tmpdir)

    get_schema_path_arg = Path(case.input_path) if is_path else str(case.input_path)
    assert [str(p) for p in _get_schema_paths(get_schema_path_arg)] == [
        # Convert to path and back to ensure normalization (e.g. running on Windows)
        str(Path(p).absolute())
        for p in case.expected_schema_paths
    ]
