import argparse
import sys

import pytest

from projects.general.countdown_timer.countdown_timer import (
    Colors,
    CountdownTimer,
    parse_arguments,
    validate_hours,
    validate_positive_int,
    validate_seconds_minutes,
)


@pytest.mark.parametrize(
    "color, expected",
    [
        (Colors.RED, "\033[31m"),
        (Colors.GREEN, "\033[32m"),
        (Colors.YELLOW, "\033[33m"),
        (Colors.CYAN, "\033[36m"),
        (Colors.RESET, "\033[0m"),
    ],
)
def test_colors(color, expected):
    """Test the color codes for terminal output."""
    text = "This is a sample text"

    assert Colors.style_text(text, color) == f"{expected}{text}\033[0m"


def test_parse_arguments():
    """Test the command-line argument parsing."""
    sys.argv = ["countdown_timer.py", "-H", "1", "-m", "15", "-s", "30"]

    args = parse_arguments()

    assert args.hours == 1
    assert args.minutes == 15
    assert args.seconds == 30


def test_validate_positive_int():
    """Test the positive integer validation."""
    assert validate_positive_int("0") == 0
    assert validate_positive_int("100") == 100


def test_validate_positive_int_exception():
    """Test the positive integer validation exception."""
    with pytest.raises(argparse.ArgumentTypeError):
        validate_positive_int("-1")


def test_validate_hours():
    """Test the hours validation."""
    assert validate_hours("0") == 0
    assert validate_hours("99") == 99


def test_validate_hours_exception():
    """Test the hours validation exception."""
    with pytest.raises(argparse.ArgumentTypeError):
        validate_hours("100")


def test_validate_seconds_minutes():
    """Test the seconds and minutes validation."""
    assert validate_hours("0") == 0
    assert validate_hours("59") == 59


def test_validate_seconds_minutes_exception():
    """Test the seconds and minutes validation exception."""
    with pytest.raises(argparse.ArgumentTypeError):
        validate_seconds_minutes("60")


@pytest.mark.parametrize(
    "params, expected",
    [
        ((1, 15, 30), (1, 15, 30, 4530)),
        ((None, 15, 30), (0, 15, 30, 930)),
        ((1, None, 30), (1, 0, 30, 3630)),
        ((1, 15, None), (1, 15, 0, 4500)),
        ((0, 0, 0), (0, 0, 0, 0)),
    ],
)
def test_countdown_timer_init(params, expected):
    """Test the CountdownTimer class initialization."""
    timer = CountdownTimer(params[0], params[1], params[2])

    assert timer.hours == expected[0]
    assert timer.minutes == expected[1]
    assert timer.seconds == expected[2]
    assert timer.total_seconds == expected[3]


@pytest.mark.parametrize(
    "params, expected",
    [
        ((1, 15, 30), 4530),
        ((None, 15, 30), 930),
        ((1, None, 30), 3630),
        ((1, 15, None), 4500),
        ((0, 0, 0), 0),
    ],
)
def test_get_total_seconds(params, expected):
    """Test the get_total_seconds method."""
    timer = CountdownTimer(params[0], params[1], params[2])

    assert timer.get_total_seconds() == expected


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (4530, "01:15:30"),
        (930, "00:15:30"),
        (3630, "01:00:30"),
        (4500, "01:15:00"),
        (0, "00:00:00"),
    ],
)
def test_format_time(seconds, expected):
    """Test the format_time method."""
    assert CountdownTimer.format_time(seconds) == expected


def test_run_timer_zero(capsys):
    """Test the run_timer method with zero countdown."""
    time = CountdownTimer(0, 0, 0)
    time.run_timer()

    captured = capsys.readouterr()
    assert "Please specify a valid countdown duration" in captured.out


def test_run_timer(capsys):
    """Test the run_timer method with a valid countdown."""
    time = CountdownTimer(0, 0, 1)
    time.run_timer()

    captured = capsys.readouterr()
    assert "Starting countdown..." in captured.out
