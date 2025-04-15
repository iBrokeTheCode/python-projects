import argparse
import time

# ================================================================
#                              COLORS
# ================================================================


class Colors:
    """Class to define color codes for terminal output."""
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

    @staticmethod
    def style_text(text: str, color: str) -> str:
        """Apply color to the text."""
        return f'{color}{text}{Colors.RESET}'

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
    """Custom type function for hours (0-99)."""
    number = validate_positive_int(value)

    if not (0 <= number <= 99):
        raise argparse.ArgumentTypeError(f'{number} must be between 0 and 99')

    return number


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments for the countdown timer app."""
    parser = argparse.ArgumentParser(description='Countdown Timer App')

    # For exclusive flags
    # group = parser.add_mutually_exclusive_group(required=True)
    # group.add_argument('--seconds', '-s', type=int, help='time in seconds')

    parser.add_argument('--hours', '-H',
                        type=validate_hours,
                        help='time in hours (0-99)')
    parser.add_argument('--minutes', '-m',
                        type=validate_seconds_minutes,
                        help='time in minutes (0-59)')
    parser.add_argument('--seconds', '-s',
                        type=validate_seconds_minutes,
                        help='time in seconds (0-59)')

    return parser.parse_args()

# ================================================================
#                         COUNTDOWN TIMER
# ================================================================


def get_total_seconds(hours: int, minutes: int, seconds: int) -> int:
    """Calculate total seconds from hours, minutes, and seconds."""
    total_seconds = 0
    if seconds:
        total_seconds += seconds
    if minutes:
        total_seconds += minutes * 60
    if hours:
        total_seconds += hours * 3600

    return total_seconds


def format_time(total_seconds: int) -> str:
    hours = total_seconds // 3600  # Calc hours
    # Calc remaining seconds and convert to minutes
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60  # Calc remaining seconds

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def run_timer(total_seconds: int):
    if total_seconds == 0:
        print(Colors.style_text(
            'Please specify a valid countdown duration', Colors.YELLOW))
        return

    print(Colors.style_text('\nStarting countdown...\n', Colors.GREEN))

    for i in range(total_seconds, 0, -1):
        print(Colors.style_text(f'> {format_time(i)}', Colors.CYAN))
        time.sleep(1)

    print(Colors.style_text("\nTime's up", Colors.RED))

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to run the countdown timer app."""
    args = parse_arguments()
    total_seconds = get_total_seconds(args.hours, args.minutes, args.seconds)
    run_timer(total_seconds)


if __name__ == '__main__':
    main()
