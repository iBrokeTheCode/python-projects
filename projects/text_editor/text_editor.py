import argparse
import pathlib

# ================================================================
#                             COLORS
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
        return f'{color}{text}{Colors.RESET}'

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filename',
        type=str,
        help='the file in the current location'
    )

    return parser.parse_args()

# ================================================================
#                           TEXT EDITOR
# ================================================================


def get_file_path(filename: str) -> pathlib.Path:
    """Constructs the absolute file path."""
    parent = pathlib.Path(__file__).parent
    return parent / filename


def check_existing_file(file_path: pathlib.Path) -> bool:
    """Checks if the file exists."""
    return file_path.exists()


def read_file(file_path: pathlib.Path) -> str:
    """Reads the contents of the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        print(Colors.style_text(f'Error reading file: {e}', Colors.RED))
        return ''


def save_file(file_path: pathlib.Path, content: str) -> None:
    """Saves the file content to the file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(Colors.style_text('File saved successfully', Colors.GREEN))
    except IOError as e:
        print(Colors.style_text(f'Error saving file: {e}', Colors.RED))


def get_user_command() -> str:
    """Gets the user's command input."""
    return input(Colors.style_text('\n❯ ', Colors.YELLOW)).strip()


def process_write_command(command: str) -> str:
    """Processes the write command."""
    return command[6:]


def process_append_command(command: str, file_content: str) -> str:
    """Processes the append command."""
    return file_content + f'\n{command[7:]}'

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the text editor."""
    args = parse_arguments()
    file_path = get_file_path(args.filename)

    if check_existing_file(file_path):
        print(Colors.style_text(
            f'\n"{args.filename}" file opened for editing', Colors.CYAN))
    else:
        try:
            pathlib.Path.touch(file_path, exist_ok=True)
            print(Colors.style_text(
                f'"{args.filename}" file created for editing', Colors.CYAN))
        except OSError as e:
            print(Colors.style_text(f'Error creating file: {e}', Colors.RED))
            return

    file_content = read_file(file_path)

    while True:
        command = get_user_command()

        if command == 'read':
            print(file_content)
        elif command.startswith('write '):
            file_content = process_write_command(command)
        elif command.startswith('append '):
            file_content = process_append_command(command, file_content)
        elif command == 'save':
            save_file(file_path, file_content)
        elif command == 'exit':
            print('Text Editor closed')
            return
        else:
            print(Colors.style_text(
                'Invalid command. Available commands (read, write <text>, append <text>, save, exit)', Colors.RED))


if __name__ == '__main__':
    main()
