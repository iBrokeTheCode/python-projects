import argparse
import pathlib

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'file',
        type=str,
        help='the file in the current location'
    )

    return parser.parse_args()

# ================================================================
#                           TEXT EDITOR
# ================================================================


def get_file_path(file: str) -> pathlib.Path:
    """Constructs the absolute file path."""
    parent = pathlib.Path(__file__).parent
    return parent / file


def check_existing_file(file_path: pathlib.Path) -> bool:
    """Checks if the file exists."""
    return file_path.exists()


def read_file(file_path: pathlib.Path) -> str:
    """Reads the contents of the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.read()
        return lines
    except IOError as e:
        print(f'Error reading file: {e}')
        return ''

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the text editor."""
    args = parse_arguments()
    file_path = get_file_path(args.file)

    print(f'(Opens {args.file} for editing)')

    if check_existing_file(file_path):
        print(read_file(file_path))
    else:
        try:
            pathlib.Path.touch(file_path, exist_ok=True)
        except OSError as e:
            print(f'Error creating file: {e}')


if __name__ == '__main__':
    main()
