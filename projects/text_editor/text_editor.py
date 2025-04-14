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
#                              UTILS
# ================================================================


def get_file_path(filename: str) -> pathlib.Path:
    """Constructs the absolute file path."""
    parent = pathlib.Path(__file__).parent
    return parent / filename

# ================================================================
#                           TEXT EDITOR
# ================================================================


class TextEditor:
    """Represents a basic text editor."""

    def __init__(self, filename: pathlib.Path):
        """Initializes a TextEditor object."""
        self.filename = filename
        self.is_saved = True
        self.file_content = ''

    def check_existing_file(self) -> bool:
        """Checks if the file exists."""
        return self.filename.exists()

    def get_user_command(self) -> str:
        """Gets the user's command input."""
        return input(Colors.style_text('\n❯ ', Colors.YELLOW)).strip()

    def open_file(self) -> None:
        """Opens or creates the file for editing."""
        if self.check_existing_file():
            print(Colors.style_text(
                f'\n"{self.filename.name}" file opened for editing', Colors.CYAN))
        else:
            try:
                pathlib.Path.touch(self.filename, exist_ok=True)
                print(Colors.style_text(
                    f'"{self.filename}" file created for editing', Colors.CYAN))
            except OSError as e:
                print(Colors.style_text(
                    f'Error creating file: {e}', Colors.RED))
                exit()

        self.file_content = self.read_file()

    def read_file(self) -> str:
        """Reads the contents of the file."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except IOError as e:
            print(Colors.style_text(f'Error reading file: {e}', Colors.RED))
            return ''

    def display_file_content(self) -> None:
        """Displays the file content."""
        if not self.is_saved:
            print(Colors.style_text(
                '*Changes not saved\n', Colors.YELLOW))
        print(Colors.style_text(self.file_content, Colors.CYAN))

    def process_write_command(self, command: str) -> None:
        """Processes the write command."""
        self.file_content = command[6:]
        self.is_saved = False

    def process_append_command(self, command: str) -> None:
        """Processes the append command."""
        self.file_content += f'\n{command[7:]}'
        self.is_saved = False

    def save_file(self) -> None:
        """Saves the file content to the file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(self.file_content)
            print(Colors.style_text('Done!', Colors.GREEN))
            self.is_saved = True
        except IOError as e:
            print(Colors.style_text(f'Error saving file: {e}', Colors.RED))

    def edit_file(self) -> None:
        """Starts the text editor and manages the command loop."""
        self.open_file()

        while True:
            command = self.get_user_command()

            if command == 'read':
                self.display_file_content()
            elif command.startswith('write '):
                self.process_write_command(command)
                print(Colors.style_text('Done!', Colors.GREEN))
            elif command.startswith('append '):
                self.process_append_command(command)
                print(Colors.style_text('Done!', Colors.GREEN))
            elif command == 'save':
                self.save_file()
            elif command == 'exit':
                print(Colors.style_text('Done. Bye!', Colors.GREEN))
                return
            else:
                print(Colors.style_text(
                    'Invalid command. Available commands (read, write <text>, append <text>, save, exit)', Colors.RED))


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to execute the text editor."""
    args = parse_arguments()
    file_path = get_file_path(args.filename)

    text_editor = TextEditor(file_path)
    text_editor.edit_file()


if __name__ == '__main__':
    main()
