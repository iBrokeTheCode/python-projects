import sys
from pathlib import Path

import pytest

from projects.general.text_editor.text_editor import (
    Colors,
    TextEditor,
    get_file_path,
    parse_arguments,
)


@pytest.mark.parametrize(
    "text, color, expected",
    [
        ("Sample text", Colors.RED, "\033[31mSample text\033[0m"),
        ("Sample text", Colors.GREEN, "\033[32mSample text\033[0m"),
        ("Sample text", Colors.YELLOW, "\033[33mSample text\033[0m"),
        ("Sample text", Colors.CYAN, "\033[36mSample text\033[0m"),
    ],
)
def test_style_text(text: str, color: str, expected: str):
    """Tests the Colors.style_text method for correct color formatting."""
    assert Colors.style_text(text, color) == expected


@pytest.mark.parametrize(
    "filename",
    [
        "my_file.txt",
        "test.txt",
        "another.txt",
    ],
)
def test_parse_arguments(filename: str):
    """Tests the parse_arguments function to ensure it correctly parses the filename."""
    sys.argv = ["text_editor.py", filename]
    args = parse_arguments()

    assert args.filename == sys.argv[1]


@pytest.mark.parametrize(
    "filename",
    [
        "my_file.txt",
        "test.txt",
        "another.txt",
    ],
)
def test_get_file_path(filename: str):
    """Tests the get_file_path function to ensure it constructs the correct absolute path."""
    file_path = get_file_path(filename)
    expected = Path(__file__).parent.parent / filename

    assert file_path == expected


def test_init_text_editor():
    """Tests the initialization of the TextEditor class."""
    file_path = get_file_path("my_file.txt")
    editor = TextEditor(file_path)

    assert editor.filename == file_path
    assert editor.is_saved == True
    assert editor.file_content == ""


@pytest.mark.parametrize(
    "filename, should_exist",
    [
        ("existing_file.txt", True),
        ("non_existent_file.txt", False),
    ],
)
def test_check_existing_file(tmp_path, filename, should_exist):
    """Tests the check_existing_file method."""
    file_path = tmp_path / filename
    if should_exist:
        file_path.touch()
    editor = TextEditor(file_path)

    assert editor.check_existing_file() == should_exist


@pytest.mark.parametrize(
    "user_input, expected",
    [
        (" read ", "read"),
        ("  write ...  ", "write ..."),
        ("   append ...  ", "append ..."),
        (" save  ", "save"),
        ("exit ", "exit"),
    ],
)
def test_get_user_command(monkeypatch, user_input, expected):
    """Tests the get_user_command method to ensure it correctly reads and strips user input."""
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    file_path = get_file_path("my_file.txt")
    editor = TextEditor(file_path)

    assert editor.get_user_command() == expected


@pytest.mark.parametrize(
    "filename, should_exist, expected_output",
    [
        ("existing_file.txt", True, "file opened for editing"),
        ("new_file.txt", False, "file created for editing"),
    ],
)
def test_open_file(capsys, tmp_path, filename, should_exist, expected_output):
    """Tests the open_file method to ensure it correctly opens existing files and creates new ones."""
    file_path = tmp_path / filename
    if should_exist:
        file_path.touch()
    editor = TextEditor(file_path)
    editor.open_file()
    captured = capsys.readouterr()

    assert expected_output in captured.out


def test_read_file(tmp_path):
    """Tests the read_file method to ensure it correctly reads the content of a file."""
    file_path = tmp_path / "test_read.txt"
    file_path.write_text("The Code to Read")
    editor = TextEditor(file_path)
    content = editor.read_file()

    assert content == "The Code to Read"


@pytest.mark.parametrize(
    "is_saved, expected_output",
    [
        (False, "*Changes not saved"),
    ],
)
def test_display_unsaved_changes_warning(capsys, tmp_path, is_saved, expected_output):
    """Tests the display_unsaved_changes_warning method."""
    file_path = tmp_path / "dummy.txt"
    editor = TextEditor(file_path)
    editor.is_saved = is_saved
    editor.display_file_content()
    captured = capsys.readouterr()

    assert expected_output in captured.out


def test_display_file_content(capsys, tmp_path):
    """Tests the display_file_content method."""
    file_path = tmp_path / "content_file.txt"
    editor = TextEditor(file_path)
    editor.file_content = "Content to display"
    editor.display_file_content()
    captured = capsys.readouterr()

    assert "Content to display" in captured.out


@pytest.mark.parametrize(
    "user_input, expected_content, expected_saved",
    [
        ("write ...", "...", False),
        ("write    ", "   ", False),
        ("write The Code", "The Code", False),
    ],
)
def test_process_write_command(tmp_path, user_input, expected_content, expected_saved):
    """Tests the process_write_command method."""
    file_path = tmp_path / "write_test.txt"
    editor = TextEditor(file_path)
    editor.process_write_command(user_input)

    assert editor.file_content == expected_content
    assert editor.is_saved is expected_saved


@pytest.mark.parametrize(
    "initial_content, user_input, expected_content, expected_saved",
    [
        ("", "append ...", "\n...", False),
        ("Initial", "append    ", "Initial\n   ", False),
        ("Initial", "append The Code", "Initial\nThe Code", False),
    ],
)
def test_process_append_command(
    tmp_path, initial_content, user_input, expected_content, expected_saved
):
    """Tests the process_append_command method."""
    file_path = tmp_path / "append_test.txt"
    editor = TextEditor(file_path)
    editor.file_content = initial_content
    editor.process_append_command(user_input)

    assert editor.file_content == expected_content
    assert editor.is_saved is expected_saved


def test_save_file(capsys, tmp_path):
    """Tests the save_file method."""
    file_path = tmp_path / "save_test.txt"
    editor = TextEditor(file_path)
    editor.file_content = "Content to save"
    editor.save_file()
    captured = capsys.readouterr()

    assert editor.is_saved is True
    assert "Done!" in captured.out
    assert file_path.read_text() == "Content to save"
