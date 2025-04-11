import json
from pathlib import Path
from typing import Any, List, Dict
from random import shuffle

# ================================================================
#                             EXCEPTIONS
# ================================================================


class QuizFileNotFoundError(Exception):
    """Exception raised when a file is not found."""

    def __init__(self, message):
        super().__init__(message)


class InvalidJsonError(Exception):
    """Exception raised when a JSON file is invalid."""

    def __init__(self, message) -> None:
        super().__init__(message)

# ================================================================
#                             CONSTANTS
# ================================================================


# TODO: Make tests
# TODO: Apply colors / Create Class
if __name__ == "__main__":
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'


# ================================================================
#                           SIMPLE QUIZ
# ================================================================

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
        raise QuizFileNotFoundError(f'File not found: "{filename}"')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise InvalidJsonError(f'Invalid JSON format in "{filename}"')


def get_user_answer(options: List[str]) -> str | None:
    """Gets and validates the user's answer."""

    user_answer_letter = input('Your answer: ').strip().lower()

    if user_answer_letter.isalpha() and len(user_answer_letter) == 1:
        try:
            user_answer = options[
                ord(user_answer_letter) - ord('a')]  # a = 97
            return user_answer
        except IndexError:
            print(
                f'\033[31mLetter "{user_answer_letter}" is not a valid option\033[0m')
            return None
    else:
        print(
            f'\033[31mLetter "{user_answer_letter}" is not a valid option\033[0m')
        return None


def play_quiz(data: List[Dict[str, Any]]) -> None:
    """Plays the quiz based on the provided data."""

    score = 0

    for index, item in enumerate(data, 1):
        # Iterate each question item in JSON data
        question = item.get('question', '')
        answer = item.get('answer', '')
        options = item.get('options', [])
        shuffle(options)

        # Display options
        print(f'\n\033[36mQuestion {index}: {question}\033[0m')
        for i, option in enumerate(options):
            print(f'{chr(97 + i)}) {option}')

        user_answer = get_user_answer(options)

        if user_answer:
            # Print answer result
            if user_answer == answer:
                print('\033[32mCorrect!\033[0m')
                score += 1
            else:
                print(
                    f'\033[31mIncorrect!\033[0m \033[32mThe correct answer is {answer}\033[0m')

        # Print score
        print(f'\033[33mYour score: {score}/{len(data)}\033[0m')


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the quiz data reader."""
    try:
        data = read_quiz_data('quiz_data.json')

        if data:
            play_quiz(data)

    except QuizFileNotFoundError as e:
        print(f'\033[31mError: {e}\033[0m')
    except InvalidJsonError as e:
        print(f'\033[31mError: {e}\033[0m')


if __name__ == '__main__':
    main()
