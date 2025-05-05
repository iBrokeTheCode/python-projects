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


class CountdownTimer:
    """A class that implements a countdown timer."""

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        """Initializes the CountdownTimer with hours, minutes, and seconds."""
        self.hours = hours or 0
        self.minutes = minutes or 0
        self.seconds = seconds or 0
        self.total_seconds = self.get_total_seconds()

    def get_total_seconds(self) -> int:
        """Calculate total seconds from hours, minutes, and seconds."""
        total_seconds = 0
        if self.seconds:
            total_seconds += self.seconds
        if self.minutes:
            total_seconds += self.minutes * 60
        if self.hours:
            total_seconds += self.hours * 3600

        return total_seconds

    @staticmethod
    def format_time(total_seconds: int) -> str:
        """Formats the remaining seconds into HH:MM:SS."""
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    def run_timer(self):
        """Runs the countdown timer."""
        if self.total_seconds == 0:
            print(Colors.style_text(
                'Please specify a valid countdown duration', Colors.YELLOW))
            return

        print(Colors.style_text('\nStarting countdown...\n', Colors.GREEN))

        try:
            for i in range(self.total_seconds, 0, -1):
                print(Colors.style_text(
                    f'> {CountdownTimer.format_time(i)}', Colors.CYAN))
                time.sleep(1)

            print(Colors.style_text("\nTime's up", Colors.YELLOW))
        except KeyboardInterrupt:
            print(Colors.style_text("\nCountdown interrupted.", Colors.RED))


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to run the countdown timer app."""
    args = parse_arguments()

    timer = CountdownTimer(args.hours, args.minutes, args.seconds)
    timer.run_timer()


if __name__ == '__main__':
    main()
