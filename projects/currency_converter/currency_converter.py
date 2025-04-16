import argparse

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Currency Converter')

    parser.add_argument(
        '--from', '-f',
        dest='from_currency',
        type=str,
        required=True,
        help='currency to convert from')

    parser.add_argument(
        '--to', '-t',
        dest='to_currency',
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
    from_currency = args.from_currency
    to_currency = args.to_currency
    amount = args.amount


if __name__ == '__main__':
    main()

# Supported currencies:
# https://api.frankfurter.dev/v1/currencies

# Currency conversion
# https://api.frankfurter.dev/v1/latest?base=${from}&symbols=${to}
