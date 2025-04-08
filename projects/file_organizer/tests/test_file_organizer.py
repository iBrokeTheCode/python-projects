import pytest
from pathlib import Path

from projects.file_organizer.file_organizer import get_cwd, directory_traversal, get_file_info


def test_get_cwd():
    assert get_cwd(__file__) == Path(__file__).parent


def test_directory_traversal():
    assert directory_traversal(Path(__file__)) == []


def test_get_file():
    assert get_file_info(Path(__file__)) == (Path(__file__).parent, Path(
        __file__).name, Path(__file__).suffix.lstrip('.').lower())
