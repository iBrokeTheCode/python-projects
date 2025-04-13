from random import randint

# ================================================================
#                             CONSTANTS
# ================================================================


class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

    @staticmethod
    def style_text(text: str, color: str) -> str:
        """Styles a message with the given color."""

        return f'{color}{text}{Colors.RESET}'


class NumberOutOfRangeError(Exception):
    """Exception raised when the user's number is out of range."""
    pass


class NumberGuessingGame:
    """Represents the Number Guessing Game."""

    RANDOM_MIN = 1
    RANDOM_MAX = 100

    ASK_NUMBER_MESSAGE = f'\nGuess a number between {RANDOM_MIN} and {RANDOM_MAX}: '
    OUT_OF_RANGE_MESSAGE = f'Your number must be between {RANDOM_MIN} and {RANDOM_MAX}'
    VALUE_ERROR_MESSAGE = 'Error: Enter a valid number value'

    def __init__(self):
        """Initializes the Number Guessing Game."""

        self.random_number = self.generate_random_number()
        self.attempts = 0

    def generate_random_number(self) -> int:
        """Generates a random number within the specified range."""

        return randint(self.RANDOM_MIN, self.RANDOM_MAX)

    def get_user_number(self) -> int:
        """Prompts the user to enter a number and validates the input."""

        while True:
            try:
                number = int(input(Colors.style_text(
                    self.ASK_NUMBER_MESSAGE, Colors.CYAN).strip()))

                if not (self.RANDOM_MIN <= number <= self.RANDOM_MAX):
                    raise NumberOutOfRangeError(self.OUT_OF_RANGE_MESSAGE)

                return number

            except ValueError:
                print(Colors.style_text(self.VALUE_ERROR_MESSAGE, Colors.RED))
            except NumberOutOfRangeError as e:
                print(Colors.style_text(f'Error: {e}', Colors.RED))

    def check_guess(self, user_number: int) -> bool:
        self.attempts += 1

        if user_number == self.random_number:
            print(Colors.style_text(
                f'\n> Congratulations! You guessed the number in {self.attempts} tries', Colors.GREEN))
            return True
        else:
            message = '> Too high!' if user_number > self.random_number else '> Too low!'
            print(Colors.style_text(message, Colors.YELLOW))
            return False

    def reset_game(self) -> None:
        self.random_number = self.generate_random_number()
        self.attempts = 0

    def play(self) -> None:
        """Plays the Number Guessing Game."""

        while True:
            user_number = self.get_user_number()

            if self.check_guess(user_number):
                keep_playing = input(
                    '\nPlay again? (y/n): ').strip().lower()

                if keep_playing in ('yes', 'y'):
                    self.reset_game()
                else:
                    break


# ================================================================
#                             MAIN
# ================================================================


def main() -> None:
    """Main function to execute the Number Guessing Game."""

    game = NumberGuessingGame()
    game.play()


if __name__ == '__main__':
    main()
