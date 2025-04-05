import pytest
from projects.text_file_analysis.text_statistics import calculate_words_count
# from projects.text_file_analysis.utils import clean_text


def test_calculate_words_count():
    text = "This is a sample text."
    assert calculate_words_count(text) == 5
