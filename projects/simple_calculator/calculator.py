import argparse
import logging

# ================================================================
#                            OPERATIONS
# ================================================================


def add(a: int, b: int) -> int: return a + b

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('sum', type=int, nargs=2, help='Sum two numbers')

    return parser.parse_args()

# ================================================================
#                             LOGGING
# ================================================================


def set_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '\n[%(asctime)s]\n(%(levelname)s): %(message)s',
        datefmt='%Y %b %d - %H:%M:%S')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

# ================================================================
#                               MAIN
# ================================================================


def main() -> None:
    logger = set_logger()
    args = parse_arguments()
    op1, op2 = args.sum[0], args.sum[1]
    if args.sum:
        logger.info(f'{op1} + {op2} = {add(op1, op2)}')


if __name__ == '__main__':
    main()
