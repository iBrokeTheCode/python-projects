import os
from pathlib import Path


def get_cwd() -> Path:
    return Path(__file__).parent


def traverse_with_os():
    cwd = get_cwd()

    for current_path, directories, files in os.walk(cwd):
        print(f'Current Path: {current_path}')
        print(f'Directories: {directories}')
        print(f'Files: {files}')
        print(f'\n{"=" * 64}\n')


def traverse_with_rglob():
    cwd = get_cwd()

    for item in cwd.rglob('*'):
        # print(item)  # All paths for files and directories
        if item.is_dir():
            print(f'Current Path: {item}')
            print(
                f'Directories: {[directory for directory in item.iterdir() if directory.is_dir()]}')
            print(
                f'Files: {[file for file in item.iterdir() if file.is_file()]}')


def create_folders():
    Path(  # Create a folder in the given path
        get_cwd() / 'parent' / 'child').mkdir(
            parents=True,  # True = No FileNotFoundError (missing parent)
            exist_ok=True  # True = No FileExistsError (already exists)
    )
