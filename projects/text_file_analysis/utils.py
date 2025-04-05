import argparse
from pathlib import Path
from string import punctuation
from re import sub


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
