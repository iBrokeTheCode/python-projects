from collections import Counter
from utils import clean_text


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


def calculate_words_frequency(text: str, number: int | None) -> dict:
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
