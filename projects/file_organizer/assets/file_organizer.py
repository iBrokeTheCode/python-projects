from pathlib import Path

# TODO: Add argparse
# TODO: Add logging
# TODO: Add tests


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


def organize_files(path: str = '') -> None:
    """Organizes files in a directory based on their extensions.

    Args:
        path: The path to the directory to organize (default: current working directory).
    """
    cwd = Path(path or get_cwd())

    # Validations
    if not cwd.exists():
        print(f'Error: Directory "{cwd}" does not exist.')
        return

    if not cwd.is_dir():
        print(f'Error: "{cwd}" is not an directory.')
        return

    extension_mapping = {
        'documents': ('txt', 'pdf', 'odf', 'docx', 'doc'),
        'images': ('png', 'jpg', 'webp', 'gif'),
        'videos': ('mp4', 'mkv', 'm4a'),
    }

    files = directory_traversal(cwd)

    # Create directories
    for folder_name in extension_mapping.keys():
        Path(cwd / folder_name).mkdir(parents=True, exist_ok=True)

    # Iterate list of files
    for file in files:
        parent, filename, extension = get_file_info(file)

        # Move/Rename file to new path
        for folder_name, extensions in extension_mapping.items():
            if extension in extensions:
                new_path = parent / folder_name / filename
                try:
                    file.rename(new_path)
                    print(
                        f'{filename} moved successfully to {new_path}')
                except Exception as e:
                    print(f'Error moving "{filename}": {e}')
                break


def main() -> None:
    test_path = '/home/alexrtc/Projects/mine/python-projects/projects/file_organizer/assets'
    organize_files(test_path)


if __name__ == '__main__':
    main()
