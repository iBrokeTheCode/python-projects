import argparse
import json
from pathlib import Path
from random import shuffle
from typing import Any

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


def read_quiz_data(filename: str) -> list[dict[str, Any]]:
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


def get_user_answer(options: list[str]) -> str | None:
    """Gets and validates the user's answer."""

    user_answer_letter = input('Your answer: ').strip().lower()

    if user_answer_letter.isalpha() and len(user_answer_letter) == 1:
        try:
            user_answer = options[
                ord(user_answer_letter) - ord('a')]  # a = 97
            return user_answer
        except IndexError:
            print(
                f'{RED}Letter "{user_answer_letter}" is not a valid option{RESET}')
            return None
    else:
        print(
            f'{RED}Letter "{user_answer_letter}" is not a valid option{RESET}')
        return None


def play_quiz(data: list[dict[str, Any]]) -> None:
    """Plays the quiz based on the provided data."""

    score = 0

    for index, item in enumerate(data, 1):
        # Iterate each question item in JSON data
        question = item.get('question', '')
        answer = item.get('answer', '')
        options = item.get('options', [])
        shuffle(options)

        # Validate fields from JSON
        if not question or not answer or not options:
            raise InvalidJsonError(
                'Incorrect format in JSON file. The fields: question, answer and options are required')

        # Display options
        print(f'\n{CYAN}Question {index}: {question}{RESET}')
        for i, option in enumerate(options):
            print(f'{chr(97 + i)}) {option}')

        user_answer = get_user_answer(options)

        if user_answer:
            # Print answer result
            if user_answer == answer:
                print(f'{GREEN}Correct!{RESET}')
                score += 1
            else:
                print(
                    f'{RED}Incorrect!{RESET} {GREEN}The correct answer is {answer}{RESET}')

        # Print score
        print(f'{YELLOW}Your score: {score}/{len(data)}{RESET}')

# ================================================================
#                              PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser(description='Play Quiz App')

    parser.add_argument(
        'quiz_data',
        type=str,
        help='a JSON file with quiz questions, answers and options'
    )

    return parser.parse_args()

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the quiz data reader."""

    args = parse_arguments()
    quiz_data = args.quiz_data

    try:
        data = read_quiz_data(quiz_data)

        if data:
            play_quiz(data)

    except QuizFileNotFoundError as e:
        print(f'{RED}Error: {e}{RESET}')
    except InvalidJsonError as e:
        print(f'{RED}Error: {e}{RESET}')


if __name__ == '__main__':
    main()
