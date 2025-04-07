# Simple File Organizer

## Description

This project involves creating a Python script that organizes files in a directory based on their file extensions. The script will traverse a given directory and move files into subdirectories corresponding to their file types (e.g., images, documents, videos).

## Features

- **Directory Traversal:** Traverse a given directory and its subdirectories.
- **File Extension Extraction:** Extract the file extension from each file.
- **Directory Creation:** Create subdirectories for each file type (if they don't already exist).
- **File Movement:** Move files into their respective subdirectories.
- **Command-Line Interface:** Use argparse to handle user input (e.g., directory path, optional flags).
- **Logging:** Implement logging to record file movements and any errors.

## Concepts Covered:

- **File System Operations:** Using the `os` and `pathlib` modules for file and directory manipulation.
- **String Manipulation:** Extracting file extensions from filenames.
- **Error Handling:** Handling potential errors during file operations.
- **Command-Line Arguments:** Using argparse to handle user input.
- **Logging:** Using the logging module to record events.

## Potential Modules

- `os` or `pathlib`: For file and directory operations.
- `argparse`: For parsing command-line arguments.
- `logging`: For logging events.

## Example Usage

```shell
python file_organizer.py /path/to/directory
python file_organizer.py /path/to/directory --log
```

## Steps

- **Set up the Project:** Create a new directory for the project and create the necessary files.
- **Implement Directory Traversal:** Use `os.walk` or `pathlib.Path.rglob` to traverse the given directory.
- **Implement File Extension Extraction:** Extract the file extension from each file.
- **Implement Directory Creation:** Create subdirectories for each file type (if they don't already exist).
- **Implement File Movement:** Move files into their respective subdirectories.
- **Implement Command-Line Arguments:** Use argparse to handle user input.
- **Implement Logging:** Use the logging module to record file movements and any errors.
- **Test and Refactor:** Test your code and refactor as needed.
