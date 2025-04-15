import argparse

# ================================================================
#                              PARSER
# ================================================================


def validate_positive_int(value: str) -> int:
    """Custom type function for positive integers."""
    number = int(value)

    if number < 0:
        raise argparse.ArgumentTypeError(
            f'{value} must be a non-negative integer')

    return number


def validate_seconds_minutes(value: str) -> int:
    """Custom type function for seconds and minutes (0-59)."""
    number = validate_positive_int(value)

    if not (0 <= number <= 59):
        raise argparse.ArgumentTypeError(f'{number} must be between 0 and 59')

    return number


def validate_hours(value: str) -> int:
    """Custom type function for hours (0-100)."""
    number = validate_positive_int(value)

    if not (0 <= number <= 100):
        raise argparse.ArgumentTypeError(f'{number} must be between 0 and 100')

    return number


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments for the countdown timer app."""
    parser = argparse.ArgumentParser(description='Countdown Timer App')

    # For exclusive flags
    # group = parser.add_mutually_exclusive_group(required=True)
    # group.add_argument('--seconds', '-s', type=int, help='time in seconds')

    parser.add_argument('--hours', '-H',
                        type=validate_hours,
                        help='time in hours (0-100)')
    parser.add_argument('--minutes', '-m',
                        type=validate_seconds_minutes,
                        help='time in minutes (0-59)')
    parser.add_argument('--seconds', '-s',
                        type=validate_seconds_minutes,
                        help='time in seconds (0-59)')

    return parser.parse_args()

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to run the countdown timer app."""
    args = parse_arguments()

    total_seconds = 0

    if args.seconds:
        total_seconds += args.seconds
    if args.minutes:
        total_seconds += args.minutes * 60
    if args.hours:
        total_seconds += args.hours * 3600

    print(f'Total seconds: {total_seconds}')


if __name__ == '__main__':
    main()
