import pytest
from projects.text_analyzer.text_statistics import (
    calculate_words_count,
    calculate_characters_count,
    calculate_lines_count,
    calculate_words_frequency,
    clean_text
)


def test_calculate_characters_count():
    text = "This is a sample text."
    assert calculate_characters_count(text) == 22


def test_calculate_words_count():
    text = "This is a sample text."
    assert calculate_words_count(text) == 5


def test_calculate_lines_count():
    text = "This is a sample text."
    assert calculate_lines_count(text) == 1


def test_calculate_words_frequency():
    text = "This is a sample text."
    assert calculate_words_frequency(
        text) == {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1}


def test_clean_text():
    text = "This is a sample text."
    assert clean_text(text) == 'this is a sample text'
