import sys

from utils import read_file, parse_arguments
from text_statistics import display_statistics


def main() -> int:
    """Main function to parse arguments and display statistics.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    try:
        args = parse_arguments()
        filename, words = args.filename, args.words

        if words is not None and words <= 0:
            print('Error: --words must be a positive integer.')
            return 1

        original_text = read_file(filename)
        display_statistics(original_text, words)
        return 0
    except FileNotFoundError as e:
        print(f'Error: {e}')
        return 1
    except Exception as e:
        print(f'Error: An unexpected error occurred: {e}')
        return 1


if __name__ == '__main__':
    sys.exit(main())

# TODO: Add testing
# TODO: Add colors
