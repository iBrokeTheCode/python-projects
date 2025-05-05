import json
import argparse
from pathlib import Path
from enum import Enum

# ================================================================
#                              TASK
# ================================================================


class Task:
    """Represents a task in the to-do list."""

    def __init__(self, title: str, completed: bool = False):
        self.__title = title
        self.__completed = completed

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @property
    def completed(self) -> bool:
        return self.__completed

    @completed.setter
    def completed(self, completed: bool) -> None:
        self.__completed = completed

    def parse_to_dict(self) -> dict:
        """Converts the task to a dictionary for JSON serialization."""

        return {
            'title': self.title,
            'completed': self.completed
        }

    def __str__(self) -> str:
        """Returns a string representation of the task."""
        return f'Task: {self.title}, Completed: {self.completed}'

# ================================================================
#                              TO DO
# ================================================================


class ToDoApp:
    """Represents a to-do list application."""
    JSON_NAME = 'data.json'

    def __init__(self):
        self.__tasks = self.load_tasks()

    @property
    def tasks(self) -> list[Task]:
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks: list[Task]) -> None:
        self.__tasks = tasks

    def add_task(self, task: Task) -> None:
        """Adds a task to the to-do list."""
        self.__tasks.append(task)
        self.save_tasks_json()

    def remove_task(self, task_index: int) -> None:
        """Removes a task from the to-do list."""
        try:
            self.__tasks.pop(task_index - 1)
            self.save_tasks_json()
        except ValueError:
            print('Error: Please enter a numeric value')
        except IndexError:
            print('Error: Please enter a valid number inside ToDo list')

    def complete_task(self, task_index: int) -> None:
        """Marks a task as completed."""
        try:
            self.__tasks[task_index - 1].completed = True
            self.save_tasks_json()
        except ValueError:
            print('Error: Please enter a numeric value')
        except IndexError:
            print('Error: Please enter a valid number inside ToDo list')

    def list_tasks(self) -> None:
        """Displays the tasks in the to-do list."""
        print('Tasks:')
        for i, task in enumerate(self.__tasks, 1):
            print(f'{i}. Title: {task.title}, Completed: {task.completed}')

    def save_tasks_json(self) -> None:
        """Saves the tasks to a JSON file."""
        cwd = Path(__file__).parent
        file_path = cwd / self.JSON_NAME

        # Create a valid Python object to serialize to JSON format (Task to dict)
        tasks_data = [task.parse_to_dict() for task in self.__tasks]

        try:
            with open(file_path, 'w') as file:
                json.dump(tasks_data, file, indent=4)
        except Exception as e:
            print(f'Failed to save tasks to JSON: {e}')

    def load_tasks(self) -> list[Task]:
        """Loads the tasks from a JSON file."""
        cwd = Path(__file__).parent
        file_path = cwd / self.JSON_NAME

        try:
            with open(file_path, 'r') as file:
                tasks_data = json.load(file)

            tasks_data = [Task(task.get('title', 'N/A'), task.get('completed', 'False'))
                          for task in tasks_data]
            return tasks_data
        except FileNotFoundError:
            # Create a new file if it doesn't exist.
            open(file_path, "w").close()
            return []
        except Exception as e:
            print(f"Failed to load tasks from json: {e}")
            return []

    def clear_tasks(self) -> None:
        """Clear all tasks from ToDoApp"""
        self.__tasks = []
        self.save_tasks_json()

# ================================================================
#                              MAIN
# ================================================================


class Command(Enum):
    """Enum for command-line commands."""
    ADD = 'add'
    LIST = 'list'
    COMPLETE = 'complete'
    REMOVE = 'remove'


def parse_arguments() -> argparse.Namespace:
    # Create a general parser
    parser = argparse.ArgumentParser(description='A Simple ToDo App')
    # Create subparser that contain parsers for each action (add, list, remove, complete)
    subparsers = parser.add_subparsers(
        dest='command', help='Available commands')

    # Add parsers to the subparser
    # Add parser
    add_parser = subparsers.add_parser(
        name=Command.ADD.value, help='Add a new task')
    add_parser.add_argument(dest='title', type=str, help='Task title')
    add_parser.add_argument(
        '--completed', action='store_true', help='Mark task as completed (default is False)')

    # List parser
    subparsers.add_parser(name=Command.LIST.value, help='List tasks')

    # Complete parser
    complete_parser = subparsers.add_parser(
        name=Command.COMPLETE.value, help='Mark task as completed')
    complete_parser.add_argument(
        dest='task_index', type=int, help='Task index')

    # Remove parser
    remove_parse = subparsers.add_parser(
        name=Command.REMOVE.value, help='Remove task')
    remove_parse.add_argument(dest='task_index', type=int, help='Task index')

    return parser.parse_args()


def main() -> None:
    app = ToDoApp()
    args = parse_arguments()
    command = args.command

    try:
        if command == Command.ADD.value:
            if args.title:
                title = args.title
                completed = args.completed if args.completed else False
                app.add_task(Task(title, completed))
            else:
                print('Error: You must provide a task title.')
        elif command == Command.LIST.value:
            app.list_tasks()
        elif command == Command.COMPLETE.value:
            app.complete_task(args.task_index)
            print(f'Task {args.task_index} completed.')
        elif command == Command.REMOVE.value:
            app.remove_task(args.task_index)
            print(f'Task {args.task_index} removed.')
        else:
            print('Error: Invalid command.')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
