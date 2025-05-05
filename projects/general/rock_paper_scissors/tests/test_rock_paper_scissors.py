import pytest

from projects.general.rock_paper_scissors.rock_paper_scissors import (
    GameOptions,
    Player,
    RockPaperScissorsGame,
)


@pytest.mark.parametrize(
    "name, expected",
    [
        ("user", ("user", 0, None)),
        ("player", ("player", 0, None)),
        ("tester", ("tester", 0, None)),
    ],
)
def test_create_player(name: str, expected: tuple[str, int, str | None]):
    """Tests the creation of a player."""
    player = Player(name)

    assert player.name == expected[0]
    assert player.score == expected[1]
    assert player.choice == expected[2]


def test_create_game():
    """Tests the creation of a game."""
    game = RockPaperScissorsGame()

    assert game.user.name == "user"
    assert game.computer.name == "computer"
    assert game.game_options == tuple(option.value for option in GameOptions)


@pytest.mark.parametrize(
    "user_choice, computer_choice, expected_winner",
    [
        (GameOptions.ROCK.value, GameOptions.SCISSORS.value, "user"),
        (GameOptions.PAPER.value, GameOptions.ROCK.value, "user"),
        (GameOptions.SCISSORS.value, GameOptions.PAPER.value, "user"),
        (GameOptions.SCISSORS.value, GameOptions.ROCK.value, "computer"),
        (GameOptions.ROCK.value, GameOptions.PAPER.value, "computer"),
        (GameOptions.PAPER.value, GameOptions.SCISSORS.value, "computer"),
        (GameOptions.PAPER.value, GameOptions.PAPER.value, None),
        (GameOptions.ROCK.value, GameOptions.ROCK.value, None),
        (GameOptions.SCISSORS.value, GameOptions.SCISSORS.value, None),
    ],
)
def test_determine_winner(
    user_choice: str, computer_choice: str, expected_winner: Player
):
    """Tests the winner determination logic."""
    game = RockPaperScissorsGame()
    game.user.choice = user_choice
    game.computer.choice = computer_choice

    winner = game.determine_winner(game.user, game.computer)

    if expected_winner == "user":
        assert winner == game.user
    elif expected_winner == "computer":
        assert winner == game.computer
    else:
        assert winner is None


def test_get_user_choice(monkeypatch):
    """Tests the user input for their choice."""
    monkeypatch.setattr("builtins.input", lambda _: "paper")
    game = RockPaperScissorsGame()

    assert game.get_user_choice() == "paper"


def test_get_computer_choice():
    """Tests the computer's random choice."""
    game = RockPaperScissorsGame()

    assert game.get_computer_choice() in tuple(option.value for option in GameOptions)


def test_play_round(monkeypatch, capsys):
    """Tests the play round function."""
    monkeypatch.setattr("builtins.input", lambda _: "scissors")
    game = RockPaperScissorsGame()
    game.play_round()

    captured = capsys.readouterr()

    assert "Computer chose:" in captured.out
    assert "won!" in captured.out or "tie" in captured.out
    assert "Score" in captured.out


def test_display_winner(capsys):
    """Tests the display winner function."""
    game = RockPaperScissorsGame()

    game.display_winner(game.user)
    captured = capsys.readouterr()
    assert "User won!" in captured.out

    game.display_winner(game.computer)
    captured = capsys.readouterr()
    assert "Computer won!" in captured.out

    game.display_winner(None)
    captured = capsys.readouterr()
    assert "It is a tie!" in captured.out


@pytest.mark.parametrize(
    "score, expected",
    [
        ((0, 0), ("0/0 victories")),
        ((7, 28), ("7/28 victories")),
        ((28, 7), ("28/7 victories")),
    ],
)
def test_display_score(capsys, score, expected):
    """Tests the display score function."""
    game = RockPaperScissorsGame()

    game.user.score = score[0]
    game.computer.score = score[1]

    game.display_scores()
    captured = capsys.readouterr()
    assert expected in captured.out
