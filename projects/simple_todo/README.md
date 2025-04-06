# Simple To-Do List Application

## Description

This project involves creating a command-line application that allows users to create, view, and manage a to-do list. The application will be designed to be user-friendly and persistent, saving and loading data to a file.

## Features

- **Add Tasks:** Allow users to add new tasks to the to-do list.
- **View Tasks:** Display the list of tasks, including their status (completed or pending).
- **Mark Tasks as Completed:** Allow users to mark tasks as completed.
- **Remove Tasks:** Allow users to remove tasks from the list.
- **Save and Load Data:** Persist the to-do list data to a file (e.g., JSON, CSV, or a simple text file).
- **Command-Line Interface:** Use `argparse` to create a user-friendly command-line interface.

## Concepts Covered

- **Lists and Dictionaries:** Using lists and dictionaries to store and manipulate task data.
- **File Handling:** Reading and writing data to files (JSON, CSV, or text).
- **Command-Line Arguments:** Using `argparse` to handle user input.
- **Data Persistence:** Saving and loading data to maintain state between application runs.

## Potential Modules

- `argparse`: For parsing command-line arguments.
- `json`: For saving and loading data in JSON format (recommended).
- `csv`: For saving and loading data in CSV format (alternative).

## Example Usage

```shell
python todo.py add "Buy groceries"
python todo.py list
python todo.py complete 1
python todo.py remove 2
```

## Steps

- **Set up the Project:** Create a new directory for the project and create the necessary files.
- **Define Data Structure:** Decide on a data structure to represent tasks (e.g., a list of dictionaries).
- **Implement Task Operations:** Implement functions or methods to add, view, complete, and remove tasks.
- **Implement File Persistence:** Implement functions or methods to save and load the to-do list data.
- **Implement Command-Line Arguments:** Use argparse to handle user input.
- **Test and Refactor:** Test your code and refactor as needed.

## Future Improvements

- Add `Enums` to task status (Pending, Completed)
