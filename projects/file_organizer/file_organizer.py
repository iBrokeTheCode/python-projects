from pathlib import Path
import argparse
import logging

# TODO: Add tests

# ================================================================
#                          FILE MANAGING
# ================================================================


def get_cwd() -> Path:
    """Returns the current working directory as a Path object."""
    return Path(__file__).parent


def directory_traversal(path: Path) -> list[Path]:
    """Traverses a directory and returns a list of file paths.

    Args:
        path: The path to the directory to traverse.

    Returns:
        A list of Path objects representing file paths.
    """
    return [item for item in path.rglob('*') if item.is_file()]


def get_file_info(file_path: Path) -> tuple[Path, str, str]:
    """Extracts file information from a file path.

    Args:
        file_path: The Path object representing the file path.

    Returns:
        A tuple containing the parent directory, filename, and extension.
    """
    parent = file_path.parent
    filename = file_path.name
    extension = file_path.suffix.lstrip('.').lower()

    return parent, filename, extension


def organize_files(path: Path, log: bool = False) -> None:
    """Organizes files in a directory based on their extensions.

    Args:
        path: The path to the directory to organize (default: current working directory).
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Validations
    if not path.exists():
        logging.error(f'Error: Directory "{path}" does not exist.')
        return

    if not path.is_dir():
        logging.error(f'Error: "{path}" is not an directory.')
        return

    extension_mapping = {
        'documents': ('txt', 'pdf', 'odf', 'docx', 'doc'),
        'images': ('png', 'jpg', 'webp', 'gif'),
        'videos': ('mp4', 'mkv', 'm4a'),
    }

    files = directory_traversal(path)

    # Create directories
    for folder_name in extension_mapping.keys():
        Path(path / folder_name).mkdir(parents=True, exist_ok=True)

    # Iterate list of files
    for file in files:
        parent, filename, extension = get_file_info(file)

        # Move/Rename file to new path
        for folder_name, extensions in extension_mapping.items():
            if extension in extensions:
                new_path = parent / folder_name / filename
                try:
                    file.rename(new_path)

                    logging.info(
                        f'{filename}" moved successfully to {new_path}')
                except Exception as e:
                    logging.error(f'Error moving "{filename}": {e}')
                break

# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Organize files in a directory')
    parser.add_argument(dest='path', type=Path, help='Directory to organize')
    parser.add_argument('--log', action='store_true',
                        help='Enable logging')

    return parser.parse_args()

# ================================================================
#                             MAIN
# ================================================================


def main() -> None:
    args = parse_arguments()

    organize_files(args.path, args.log)


if __name__ == '__main__':
    main()
