import argparse

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Currency Converter')

    parser.add_argument(
        '--from', '-f',
        type=str,
        required=True,
        help='currency to convert from')

    parser.add_argument(
        '--to', '-t',
        type=str,
        required=True,
        help='currency to convert to'
    )

    parser.add_argument(
        '--amount', '-a',
        type=float,
        required=True,
        help='amount to convert'
    )

    return parser.parse_args()

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    args = parse_arguments()
    print(args)


if __name__ == '__main__':
    main()
