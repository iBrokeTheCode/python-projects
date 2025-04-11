import json
from pathlib import Path
from pprint import pprint
from typing import Any, List, Dict


# ================================================================
#                             PARSER
# ================================================================

class FileNotFoundError(Exception):
    """Exception raised when a file is not found."""

    def __init__(self, message):
        super().__init__(message)


class InvalidJsonError(Exception):
    """Exception raised when a JSON file is invalid."""

    def __init__(self, message) -> None:
        super().__init__(message)


def get_cwd_path() -> Path:
    """Returns the current working directory as a Path object."""

    return Path(__file__).parent


def read_quiz_data(filename: str) -> List[Dict[str, Any]]:
    """
    Reads quiz data from a JSON file.

    Args:
        filename: The name of the JSON file.

    Returns:
        A list of dictionaries representing the quiz data, or None if the file is not found.
    """
    file_path = get_cwd_path() / filename

    if not file_path.exists():
        raise FileNotFoundError(f'File not found: "{filename}"')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise InvalidJsonError(f'Invalid JSON format in "{filename}"')

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the quiz data reader."""
    try:
        data = read_quiz_data('quiz_data.json')

        if data:
            pprint(data)
    except FileNotFoundError as e:
        print(f'\033[31mError: {e}\033[0m')
    except InvalidJsonError as e:
        print(f'\033[31mError: {e}\033[0m')


if __name__ == '__main__':
    main()
