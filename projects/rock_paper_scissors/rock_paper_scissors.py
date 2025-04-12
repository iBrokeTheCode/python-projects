from enum import Enum
from typing import Literal, cast

# ================================================================
#                            CONSTANTS
# ================================================================


class Colors:
    """Class to define color codes for terminal output."""

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

    @staticmethod
    def style_message(color: str, message: str) -> str:
        """Styles a message with the given color."""

        return f'{color}{message}{Colors.RESET}'


class GameOptions(Enum):
    """Enum to represent game options."""

    PAPER = 'paper'
    ROCK = 'rock'
    SCISSORS = 'scissors'

# ================================================================
#                          ROCK PAPER SCISSORS
# ================================================================


def ask_user_play() -> Literal['paper', 'rock', 'scissors']:
    options = tuple(option.value for option in GameOptions)

    while (user_play := input(f'{Colors.CYAN}Enter your choice (rock, paper, scissors): {Colors.RESET}').strip().lower()) not in options:
        print(Colors.style_message(
            color=Colors.RED,
            message='Enter a valid play(rock, paper, scissors)\n')
        )

    return cast(Literal['paper', 'rock', 'scissors'], user_play)


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the rock paper scissors user input."""

    user_play = ask_user_play()
    print(Colors.style_message(
        color=Colors.GREEN,
        message=f'Your choice is: {user_play}')
    )


if __name__ == '__main__':
    main()
