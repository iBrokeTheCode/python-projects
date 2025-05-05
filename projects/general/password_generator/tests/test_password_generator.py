import re
import sys

import pytest

from projects.general.password_generator.password_generator import (
    generate_password,
    main,
    parse_arguments,
)


@pytest.mark.parametrize(
    "args, expected",
    [
        (["password_generator.py"], [None, False, False, False, False]),
        (
            [
                "password_generator.py",
                "--length",
                "12",
                "--uppercase",
                "--lowercase",
                "--digits",
                "--symbols",
            ],
            (12, True, True, True, True),
        ),
        (
            ["password_generator.py", "-l", "16", "-u", "-d"],
            (16, True, False, True, False),
        ),
    ],
)
def test_parse_arguments(args, expected):
    """Tests the gotten parsed arguments from argparse"""

    sys.argv = args
    parsed_arguments = parse_arguments()

    assert parsed_arguments.length == expected[0]
    assert parsed_arguments.uppercase == expected[1]
    assert parsed_arguments.lowercase == expected[2]
    assert parsed_arguments.digits == expected[3]
    assert parsed_arguments.symbols == expected[4]


@pytest.mark.parametrize(
    "params, expected",
    [
        ((-7, False, False, False, False), 8),
        ((0, False, False, False, False), 8),
        ((7, False, False, False, False), 8),
        ((28, False, False, False, False), 28),
    ],
)
def test_generate_password_length(params, expected):
    """Tests the length of generated passwords."""

    assert len(generate_password(*params)) == expected


@pytest.mark.parametrize(
    "params, expected_patterns",
    [
        ((8, True, False, False, False), r"[A-Z]"),  # Uppercase
        ((8, False, True, False, False), r"[a-z]"),  # Lowercase
        ((8, False, False, True, False), r"\d"),  # Digits
        (
            (8, False, False, False, True),
            r"[!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]",
        ),  # Symbols
        (
            (8, True, True, True, True),
            r"[A-Za-z\d!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]",
        ),  # all
    ],
)
def test_generate_password_characters(params, expected_patterns):
    """Tests if generated passwords contain the required character sets."""
    password = generate_password(*params)

    assert re.search(expected_patterns, password) is not None


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            ["password_generator.py", "-l", "-5"],
            "Password must be at least 8 length. Set to 8 characters",
        ),
        (["password_generator.py"], "Your password: "),
        (["password_generator.py", "-l", "16"], "Your password: "),
    ],
)
def test_main_invalid_length(capsys, args, expected):
    """Tests the output message after running the main function."""
    sys.argv = args

    main()
    captured = capsys.readouterr()
    assert expected in captured.out
