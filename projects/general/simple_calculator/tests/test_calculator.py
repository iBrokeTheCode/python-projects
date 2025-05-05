import logging
import sys

import pytest

from projects.general.simple_calculator.calculator import (
    add,
    division,
    parse_arguments,
    product,
    setup_logger,
    subtract,
)

# ================================================================
#                            OPERATIONS
# ================================================================


@pytest.mark.parametrize(
    "a, b, expected", [(28, 7, 35), (-28, 7, -21), (0, 7, 7), (28, 0, 28)]
)
def test_sum(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(28, 7, 21), (-28, 7, -35), (0, 7, -7), (28, 0, 28)]
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(28, 7, 196), (-28, 7, -196), (0, 7, 0), (28, 0, 0)]
)
def test_product(a, b, expected):
    assert product(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (28, 7, 4.0),
        (-28, 7, -4.0),
        (0, 7, 0),
    ],
)
def test_division(a, b, expected):
    assert division(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(28, 0)


# ================================================================
#                            PARSER
# ================================================================


def test_parse_arguments_sum():
    sys.argv = ["calculator.py", "sum", "10", "5"]
    args = parse_arguments()
    assert args.operation == "sum"
    assert args.operands == [10, 5]


# ================================================================
#                            LOGGING
# ================================================================


def test_setup_logger():
    logger = setup_logger()
    assert isinstance(logger, logging.Logger)
    assert len(logger.handlers) > 0
    assert isinstance(logger.handlers[0], logging.StreamHandler)
