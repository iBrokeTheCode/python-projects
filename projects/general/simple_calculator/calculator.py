import argparse
import logging
from enum import Enum
from typing import Union, Dict, Callable

# ================================================================
#                           ENUM CLASS
# ================================================================


class Operation(Enum):
    """Enumeration for supported arithmetic operations."""
    SUM = 'sum'
    SUBTRACT = 'subtract'
    PRODUCT = 'product'
    DIVISION = 'division'


# ================================================================
#                            OPERATIONS
# ================================================================


def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts two integers."""
    return a - b


def product(a: int, b: int) -> int:
    """Multiplies two integers."""
    return a * b


def division(a: int, b: int) -> Union[int, float]:
    """Divides two integers, handling division by zero."""
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description='Simple Calculator')
    sub_parsers = parser.add_subparsers(
        dest='operation', description='Available operations')

    sum_parser = sub_parsers.add_parser(
        Operation.SUM.value, help='Sum 2 numbers')
    sum_parser.add_argument('operands', nargs=2, type=int)

    subtract_parser = sub_parsers.add_parser(
        Operation.SUBTRACT.value, help='Subtract 2 numbers')
    subtract_parser.add_argument('operands', nargs=2, type=int)

    product_parser = sub_parsers.add_parser(
        Operation.PRODUCT.value, help='Multiply 2 numbers')
    product_parser.add_argument('operands', nargs=2, type=int)

    division_parser = sub_parsers.add_parser(
        Operation.DIVISION.value, help='Divide 2 numbers')
    division_parser.add_argument('operands', nargs=2, type=int)

    return parser.parse_args()

# ================================================================
#                             LOGGING
# ================================================================


def setup_logger() -> logging.Logger:
    """Sets up and returns a logger instance."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '\n[%(asctime)s]\n(%(levelname)s): %(message)s',
        datefmt='%Y %b %d - %H:%M:%S'
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

# ================================================================
#                               MAIN
# ================================================================


def main() -> None:
    """Main function to execute the calculator."""
    logger = setup_logger()
    args = parse_arguments()

    if not args.operation:
        logger.error('No operation specified. USe --help for options')
        return

    op1, op2 = args.operands[0], args.operands[1]

    operations: Dict[Operation, Callable[[int, int], Union[int, float]]] = {
        Operation.SUM: add,
        Operation.SUBTRACT: subtract,
        Operation.PRODUCT: product,
        Operation.DIVISION: division
    }

    try:
        result = operations[Operation(args.operation)](op1, op2)
        logger.info(f'Result = {result}')
    except KeyError:
        logger.error('Invalid operation. Use --help for options.')
    except ValueError as e:
        logger.error(str(e))
    except Exception as e:
        logger.error(f'An unexpected error occurred: {e}')


if __name__ == '__main__':
    main()
