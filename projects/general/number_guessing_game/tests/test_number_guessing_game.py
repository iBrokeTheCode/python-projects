import pytest

from projects.general.number_guessing_game.number_guessing_game import (
    Colors,
    NumberGuessingGame,
)


@pytest.mark.parametrize(
    "color, code",
    [
        (Colors.RED, "\033[31m"),
        (Colors.GREEN, "\033[32m"),
        (Colors.YELLOW, "\033[33m"),
        (Colors.CYAN, "\033[36m"),
    ],
)
def test_colors(color: str, code: str):
    """Tests the Colors.style_text method for correct color formatting."""
    text = "This is a sample text"
    expected = f"{code}{text}\033[0m"
    assert Colors.style_text(text, color) == expected


def test_game_init():
    """Tests the initialization of the NumberGuessingGame class."""
    game = NumberGuessingGame()

    assert game.attempts == 0
    assert game.RANDOM_MIN <= game.random_number <= game.RANDOM_MAX


def test_generate_random_number():
    """Tests the generate_random_number method."""
    game = NumberGuessingGame()

    assert game.RANDOM_MIN <= game.random_number <= game.RANDOM_MAX


def test_get_user_number(monkeypatch):
    """Tests the get_user_number method for valid and invalid inputs."""
    game = NumberGuessingGame()

    # Test valid input after invalid inputs
    inputs = ["text", "-10", "150", "50"]
    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    assert game.get_user_number() == 50


def test_get_user_number_with_output(monkeypatch, capsys):
    """Tests the get_user_number method for valid and invalid inputs, and output."""
    game = NumberGuessingGame()

    # Test invalid input (non-numeric)
    inputs = ("text", "50")
    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    assert game.get_user_number() == 50
    captured = capsys.readouterr()
    assert "Enter a valid number" in captured.out

    # Test input out of range (lower bound)
    inputs = ("-10", "50")
    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    assert game.get_user_number() == 50
    captured = capsys.readouterr()
    assert "Your number must be between" in captured.out

    # Test input out of range (upper bound)
    inputs = ("150", "50")
    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    assert game.get_user_number() == 50
    captured = capsys.readouterr()
    assert "Your number must be between" in captured.out


@pytest.mark.parametrize(
    "guess, expected, message",
    [
        (50, True, "Congratulations!"),
        (25, False, "Too low!"),
        (75, False, "Too high!"),
    ],
)
def test_check_guess(monkeypatch, capsys, guess, expected, message):
    game = NumberGuessingGame()
    game.random_number = 50

    assert game.check_guess(guess) == expected
    captured = capsys.readouterr()
    assert message in captured.out


def test_reset_game():
    game = NumberGuessingGame()
    game.reset_game()

    assert game.RANDOM_MIN <= game.random_number <= game.RANDOM_MAX
    assert game.attempts == 0
