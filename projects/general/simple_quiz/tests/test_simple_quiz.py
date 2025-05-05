import sys
from pathlib import Path

import pytest

from projects.general.simple_quiz.simple_quiz import (
    InvalidJsonError,
    QuizFileNotFoundError,
    get_cwd_path,
    get_user_answer,
    parse_arguments,
    play_quiz,
    read_quiz_data,
)


def test_parse_arguments():
    """Tests the gotten parsed arguments from argparse"""

    sys.argv = ["simple_quiz.py", "quiz_data.json"]

    args = parse_arguments()

    assert args.quiz_data == "quiz_data.json"


def test_get_cwd_path():
    """Tests the gotten current working directory"""
    assert get_cwd_path(__file__) == Path(__file__).parent


def test_read_quiz_data_ok():
    """Tests the read_quiz_data function and check if it get the expected data"""

    expected = [
        {
            "question": "Question",
            "options": ["Option 1", "Option 2", "Option 3"],
            "answer": "Answer",
        }
    ]

    assert read_quiz_data("test_ok.json") == expected


def test_read_quiz_data_not_exist():
    """Tests the read_quiz_data function and check if raise an error for unexistent file"""

    with pytest.raises(QuizFileNotFoundError):
        read_quiz_data("404.json")


def test_read_quiz_data_invalid():
    """Tests the read_quiz_data function and check if raise an error for invalid JSON format"""

    with pytest.raises(InvalidJsonError):
        read_quiz_data("test_invalid_json.json")


@pytest.mark.parametrize(
    "user_answer_letter, expected",
    [
        ("a", "option a"),
        ("z", None),
        ("abc", None),
    ],
)
def test_get_user_answer(monkeypatch, user_answer_letter, expected):
    """Tests the get_user_answer function"""

    OPTIONS = ["option a", "option b", "option c"]

    # Simulate user input
    monkeypatch.setattr("builtins.input", lambda _: user_answer_letter)
    assert get_user_answer(OPTIONS) == expected


@pytest.mark.parametrize(
    "answer, expected",
    [
        ("b", "Correct!"),
        ("a", "Incorrect!"),
    ],
)
def test_play_quiz(monkeypatch, capsys, answer, expected):
    """Tests the play_quiz function."""

    quiz_data = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin"],
            "answer": "Paris",
        },
    ]

    monkeypatch.setattr("builtins.input", lambda _: answer)
    play_quiz(quiz_data)
    captured = capsys.readouterr()

    assert expected in captured.out


def test_play_quiz_error():
    """Tests the play_quiz function with invalid fields."""

    quiz_data = [
        {
            "question_different": "What is the capital of France?",
            "options_different": ["London", "Paris", "Berlin"],
            "answer_different": "Paris",
        },
    ]

    with pytest.raises(InvalidJsonError):
        play_quiz(quiz_data)
