import argparse

# ================================================================
#                           UNITS CONVERSION
# ================================================================

LENGTH_UNITS = {
    'meters': 1.0,
    'feet': 3.28084,
    'inches': 39.3701,
    'centimeters': 100.0,
    'millimeters': 1000.0,
    'kilometers': 0.001,
    'miles': 0.000621371,
}

TEMPERATURE_UNITS = {
    'celsius': 1.0,
    'fahrenheit': 1.0,
    'kelvin': 1.0,
}

WEIGHT_UNITS = {
    'kilograms': 1.0,
    'grams': 1000.0,
    'pounds': 2.20462,
    'ounces': 35.274,
}

UNIT_CATEGORIES = {
    'length': LENGTH_UNITS,
    'temperature': TEMPERATURE_UNITS,
    'weight': WEIGHT_UNITS
}


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin: float) -> float:
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


TEMPERATURE_CONVERSIONS = {
    ('celsius', 'fahrenheit'): celsius_to_fahrenheit,
    ('fahrenheit', 'celsius'): fahrenheit_to_celsius,
    ('celsius', 'kelvin'): celsius_to_kelvin,
    ('kelvin', 'celsius'): kelvin_to_celsius,
    ('fahrenheit', 'kelvin'): fahrenheit_to_kelvin,
    ('kelvin', 'fahrenheit'): kelvin_to_fahrenheit,
}

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser(description='Unit Converter')

    parser.add_argument(
        '--category',
        type=str,
        required=True,
        choices=UNIT_CATEGORIES.keys(),
        help='unit category'
    )

    parser.add_argument(
        '--from',
        dest='from_unit',
        type=str,
        required=True,
        help='the original unit',
    )
    parser.add_argument(
        '--to',
        dest='to_unit',
        type=str,
        required=True,
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


def convert_units(category: str, from_unit: str, to_unit: str, value: float) -> float:
    """Converts a value from one unit to another within a specified category."""

    UNITS = UNIT_CATEGORIES[category]

    if from_unit not in UNITS.keys():
        raise ValueError('--from unit no supported')
    if to_unit not in UNITS.keys():
        raise ValueError('--to unit no supported')

    if category == 'temperature':
        if (from_unit, to_unit) in TEMPERATURE_CONVERSIONS.keys():
            conversion_function = TEMPERATURE_CONVERSIONS[(from_unit, to_unit)]
            return conversion_function(value)
        else:
            raise ValueError(f'{from_unit} to {to_unit} no supported')
    else:
        conversion_factor = UNITS[to_unit] / UNITS[from_unit]
        return value * conversion_factor


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the unit converter."""

    args = parse_arguments()
    category = args.category
    from_unit = args.from_unit
    to_unit = args.to_unit
    value = args.value

    try:
        result = convert_units(category, from_unit, to_unit, value)

        print(
            '\033[32m{} {} is equal to {} {}\033[0m'.format(value, from_unit, result, to_unit))
    except ValueError as e:
        print(f'\033[31mValue Error: {e}\033[0m')
    except Exception as e:
        print(f'\033[31mAn unexpected error occurred: {e}\033[0m')


if __name__ == '__main__':
    main()
