import argparse

# ================================================================
#                               DATA
# ================================================================

AVAILABLE_UNITS = ('meters', 'feet', 'inches', 'centimeters',
                   'millimeters', 'kilometers', 'miles')

length_units = {
    'meters': 1.0,
    'feet': 3.28084,
    'inches': 39.3701,
    'centimeters': 100.0,
    'millimeters': 1000.0,
    'kilometers': 0.001,
    'miles': 0.000621371,
}

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Unit Converter')

    parser.add_argument(
        '--from',
        dest='from_unit',
        type=str,
        required=True,
        choices=AVAILABLE_UNITS,
        help='the original unit',
    )
    parser.add_argument(
        '--to',
        dest='to_unit',
        type=str,
        required=True,
        choices=AVAILABLE_UNITS,
        help='the target unit'
    )
    parser.add_argument(
        '--value',
        type=float,
        required=True,
        help='the value to convert'
    )

    return parser.parse_args()

# ================================================================
#                            CONVERSION
# ================================================================


def convert_units(from_unit: str, to_unit: str, value: float) -> float:
    conversion_factor = length_units[to_unit] / length_units[from_unit]
    return value * conversion_factor


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    args = parse_arguments()
    from_unit, to_unit, value = args.from_unit, args.to_unit, args.value

    result = convert_units(from_unit, to_unit, value)

    print(
        '{} {} is equal to {} {}'.format(value, from_unit, result, to_unit))


if __name__ == '__main__':
    main()
