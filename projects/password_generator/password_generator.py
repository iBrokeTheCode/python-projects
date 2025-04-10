import argparse

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments for the password generator."""

    parser = argparse.ArgumentParser(description='Password Generator')

    parser.add_argument(
        '-l', '--length',
        type=int,
        help='the length of the password',
        required=True,
        metavar='length'
    )

    parser.add_argument(
        '-u', '--uppercase',
        help='include uppercase letters',
        action='store_true'
    )

    parser.add_argument(
        '-w', '--lowercase',
        help='include lowercase letters',
        action='store_true'
    )

    parser.add_argument(
        '-d', '--digits',
        help='include digits',
        action='store_true'
    )

    parser.add_argument(
        '-s', '--symbols',
        help='include symbols',
        action='store_true'
    )

    return parser.parse_args()


def main() -> None:
    """Main function to execute the password generator."""

    args = parse_arguments()
    print(args)


if __name__ == '__main__':
    main()
