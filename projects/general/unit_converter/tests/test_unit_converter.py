import sys

import pytest

from projects.general.unit_converter.unit_converter import (
    convert_units,
    main,
    parse_arguments,
)


def test_parse_arguments():
    sys.argv = [
        "unit_converter.py",
        "--category",
        "length",
        "--from",
        "meters",
        "--to",
        "centimeters",
        "--value",
        "1",
    ]
    args = parse_arguments()
    assert args.category == sys.argv[2]
    assert args.from_unit == sys.argv[4]
    assert args.to_unit == sys.argv[6]
    assert args.value == float(sys.argv[8])


@pytest.mark.parametrize(
    "category, from_unit, to_unit, value, expected",
    [
        ("length", "meters", "centimeters", 1, 100.0),
        ("weight", "kilograms", "grams", 1, 1000.0),
        ("temperature", "celsius", "fahrenheit", 1, 33.8),
    ],
)
def test_convert_units(category, from_unit, to_unit, value, expected):
    assert convert_units(category, from_unit, to_unit, value) == expected


@pytest.mark.parametrize(
    "category, from_unit, to_unit, value",
    [
        ("length", "meter", "centimeters", 1),
        ("weight", "kilograms", "gram", 1),
        ("temperature", "c", "f", 1),
    ],
)
def test_convert_units_exceptions(category, from_unit, to_unit, value):
    with pytest.raises(ValueError):
        convert_units(category, from_unit, to_unit, value)


def test_main_valid_conversion(capsys):
    sys.argv = [
        "unit_converter.py",
        "--category",
        "length",
        "--from",
        "meters",
        "--to",
        "centimeters",
        "--value",
        "1",
    ]
    main()
    captured = capsys.readouterr()
    assert "1.0 meters is equal to 100.0 centimeters" in captured.out


def test_main_invalid_unit(capsys):
    sys.argv = [
        "unit_converter.py",
        "--category",
        "length",
        "--from",
        "meter",
        "--to",
        "centimeters",
        "--value",
        "1",
    ]
    main()
    captured = capsys.readouterr()
    assert "Value Error: --from unit no supported" in captured.out
