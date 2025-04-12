from enum import Enum
from random import choice
from typing import Literal, cast

# ================================================================
#                            CONSTANTS
# ================================================================


class GameOptions(Enum):
    """Enum to represent game options."""

    PAPER = 'paper'
    ROCK = 'rock'
    SCISSORS = 'scissors'


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


TIE_MESSAGE = Colors.style_message(Colors.YELLOW, 'It is a tie!')
PLAY_AGAIN_MESSAGE = Colors.style_message(
    Colors.CYAN, '\nDo you want to play again? (yes/no): ')
INVALID_INPUT_MESSAGE = Colors.style_message(
    Colors.RED, 'Enter a valid play (rock, paper, scissors).\n')


# ================================================================
#                          ROCK PAPER SCISSORS
# ================================================================


class Player:
    """Represents a player in the Rock, Paper, Scissors game."""

    def __init__(self, name: str, score: int = 0, choice: str = ''):
        self.name = name
        self.score = score
        self.choice = choice


class RockPaperScissorsGame:
    """Represents the Rock, Paper, Scissors game."""

    def __init__(self):
        self.user = Player('user')
        self.computer = Player('computer')
        self.game_options = tuple(option.value for option in GameOptions)

    def get_user_choice(self) -> Literal['paper', 'rock', 'scissors']:
        """Prompts the user to enter their choice."""

        while (user_play := input(
                f'\n{Colors.CYAN}Enter your choice (rock, paper, scissors): {Colors.RESET}').strip().lower()) not in self.game_options:
            print(INVALID_INPUT_MESSAGE)

        return cast(Literal['paper', 'rock', 'scissors'], user_play)

    def get_computer_choice(self) -> Literal['paper', 'rock', 'scissors']:
        """Generates a random choice for the computer."""

        computer_choice = choice(self.game_options)
        return cast(Literal['paper', 'rock', 'scissors'], computer_choice)

    def determine_winner(self, player1: Player, player2: Player) -> Player | None:
        """Determines the winner of the round."""

        if player1.choice == player2.choice:
            return None
        elif (player1.choice, player2.choice) in (
            (GameOptions.ROCK.value, GameOptions.SCISSORS.value),
            (GameOptions.PAPER.value, GameOptions.ROCK.value),
            (GameOptions.SCISSORS.value, GameOptions.PAPER.value),
        ):
            return player1
        else:
            return player2

    def display_winner(self, winner: Player | None) -> None:
        """Displays the winner of the round."""
        if not winner:
            print(TIE_MESSAGE)
        else:
            print(Colors.style_message(Colors.YELLOW,
                  f'{winner.name.capitalize()} won!'))

    def display_scores(self) -> None:
        """Displays the scores of the players."""
        print(Colors.style_message(Colors.GREEN,
              f'Score [{self.user.name}/{self.computer.name}]: {self.user.score}/{self.computer.score} victories'))

    def play_round(self) -> None:
        """Plays a single round of the game."""

        self.user.choice = self.get_user_choice()
        self.computer.choice = self.get_computer_choice()

        print(Colors.style_message(Colors.CYAN,
              'Computer chose:'), self.computer.choice)

        winner = self.determine_winner(self.user, self.computer)

        if winner:
            winner.score += 1

        self.display_winner(winner)
        self.display_scores()

    def start_game(self) -> None:
        """Starts the Rock, Paper, Scissors game."""

        while True:
            self.play_round()

            keep_playing = input(Colors.style_message(
                Colors.CYAN, PLAY_AGAIN_MESSAGE)).strip().lower()

            if keep_playing != 'yes':
                break


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the rock paper scissors user input."""
    game = RockPaperScissorsGame()
    game.start_game()


if __name__ == '__main__':
    main()
