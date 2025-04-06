import argparse

from collections import Counter
from pathlib import Path
from string import punctuation
from re import sub


def calculate_words_count(text: str) -> int:
    """Calculates the number of words in the given text.

    Args:
        text: The text to analyze.

    Returns:
        The number of words in the text.
    """
    cleaned_text = clean_text(text)

    return len(cleaned_text.split())


def calculate_lines_count(text: str) -> int:
    """Calculates the number of lines in the given text.

    Args:
        text: The text to analyze.

    Returns:
        The number of lines in the text.
    """
    return len(text.splitlines())


def calculate_characters_count(text: str) -> int:
    """Calculates the total number of characters in the given text.

    Args:
        text: The text to analyze.

    Returns:
        The total number of characters in the text.
    """
    return len(text)


def calculate_words_frequency(text: str, number: int | None = None) -> dict:
    """Calculates the frequency of each word in the given text.

    Args:
        text: The text to analyze.
        number: Optional number of most frequent words to return.

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    return dict(Counter(words).most_common(number))


def display_statistics(text: str, number: int | None) -> None:
    """Displays text statistics in a formatted table.

    Args:
        text: The text to analyze.
        number: Optional number of most frequent words to display.
    """
    from terminal_colors import TerminalColors, colored_print

    colored_print(f'\n{"Number of":^20}{"Count":^20}',
                  TerminalColors.FG_CYAN, bold=True)
    colored_print('-' * 40, TerminalColors.FG_CYAN)

    print(f'{"words":<20}{calculate_words_count(text):^20}')
    print(f'{"lines":<20}{calculate_lines_count(text):^20}')
    print(f'{"characters":<20}{calculate_characters_count(text):^20}')

    colored_print(f'\n{"Words Frequency":^42}',
                  TerminalColors.FG_YELLOW, bold=True)
    colored_print('-' * 40, TerminalColors.FG_YELLOW)

    words_frequency = calculate_words_frequency(text, number)

    for word, frequency in words_frequency.items():
        print(f'{word:<20}   {frequency:^20}')

# ================================================================
#                              UTILS
# ================================================================


def read_file(filename: str) -> str:
    """Reads the content of a file and returns it as a string.

    Args:
        filename: The name of the file to read.

    Returns:
        The content of the file as a string.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    current_directory = Path(__file__).parent
    file_path = current_directory / filename

    try:
        with open(file_path, 'r') as file:
            lines = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'"{filename}" file not found')
    else:
        return lines


def clean_text(text: str) -> str:
    """Cleans the text by lowercasing, removing punctuation, and replacing newlines with spaces.

    Args:
        text: The text to clean.

    Returns:
        The cleaned text.
    """
    text = text.strip().lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', punctuation))
    # Replace newlines and indentation with spaces
    text = sub(r'\s+', ' ', text)
    return text


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Text File Analysis Tool')

    parser.add_argument('filename',
                        type=str,
                        help='filename in the current working directory')

    parser.add_argument('--words',
                        type=int,
                        help='number of most frequent words')

    return parser.parse_args()
