import json
import argparse
from pathlib import Path

# ================================================================
#                              TASK
# ================================================================

# TODO: Add enum to argparse options
# TODO: Add tests
# TODO: Improve code and add docstrings


class Task:
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
        return {
            'title': self.title,
            'completed': self.completed
        }

    def __str__(self) -> str:
        return f'Task: {self.title}'

# ================================================================
#                              TO DO
# ================================================================


class ToDoApp:
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
        self.__tasks.append(task)
        self.save_tasks_json()

    def remove_task(self, task_index: int) -> None:
        try:
            self.__tasks.pop(task_index - 1)
            self.save_tasks_json()
        except ValueError:
            print('Error: Please enter a numeric value')
        except IndexError:
            print('Error: Please enter a valid number inside ToDo list')

    def complete_task(self, task_index: int) -> None:
        try:
            self.__tasks[task_index - 1].completed = True
            self.save_tasks_json()
        except ValueError:
            print('Error: Please enter a numeric value')
        except IndexError:
            print('Error: Please enter a valid number inside ToDo list')

    def view_tasks(self) -> None:
        print('Tasks:')
        for i, task in enumerate(self.__tasks, 1):
            print(f'{i}. Title: {task.title}, Completed: {task.completed}')

    def save_tasks_json(self) -> None:
        cwd = Path(__file__).parent
        file_path = cwd / self.JSON_NAME

        # Create a valid Python object to serialize to JSON format (Task to dict)
        tasks_data = [task.parse_to_dict() for task in self.__tasks]

        try:
            with open(file_path, 'w') as file:
                json.dump(tasks_data, file, indent=4)
        except Exception as e:
            print(f'Error: {e}')

    def load_tasks(self) -> list[Task]:
        cwd = Path(__file__).parent
        file_path = cwd / self.JSON_NAME

        try:
            with open(file_path, 'r') as file:
                tasks_data = json.load(file)

            tasks_data = [Task(task.get('title'), task.get('completed'))
                          for task in tasks_data]
            return tasks_data
        except FileNotFoundError:
            open(file_path, "w").close()
            return []
        except Exception:
            return []

# ================================================================
#                              MAIN
# ================================================================


def parse_arguments() -> argparse.Namespace:
    # Create a general parser
    parser = argparse.ArgumentParser(description='A Simple ToDo App')
    # Create subparser that contain parsers for each action (add, list, remove, complete)
    subparsers = parser.add_subparsers(
        dest='command', help='Available commands')

    # Add parsers to the subparser
    # Add parser
    add_parser = subparsers.add_parser(name='add', help='Add a new task')
    add_parser.add_argument(dest='title', type=str, help='Task title')
    add_parser.add_argument(
        '--completed', action='store_true', help='Mark task as completed (default is False)')

    # List parser
    subparsers.add_parser(name='list', help='List tasks')

    # Complete parser
    complete_parser = subparsers.add_parser(
        name='complete', help='Mark task as completed')
    complete_parser.add_argument(
        dest='task_index', type=int, help='Task index')

    # Remove parser
    remove_parse = subparsers.add_parser(name='remove', help='Remove task')
    remove_parse.add_argument(dest='task_index', type=int, help='Task index')

    return parser.parse_args()


def main() -> None:
    app = ToDoApp()
    args = parse_arguments()
    command = args.command

    if command == 'add':
        if args.title:
            title = args.title
            completed = args.completed if args.completed else False
            app.add_task(Task(title, completed))
        else:
            print('You must pass a title for the task')
    elif command == 'list':
        app.view_tasks()
    elif command == 'complete':
        if args.task_index:
            app.complete_task(args.task_index)
        else:
            print('Pass a valid task index please')
    elif command == 'remove':
        if args.task_index:
            app.remove_task(args.task_index)
        else:
            print('Pass a valid task index please')
    else:
        print('Pass a valid command')


if __name__ == '__main__':
    main()
