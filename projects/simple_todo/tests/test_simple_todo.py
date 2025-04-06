import pytest
from pathlib import Path

from projects.simple_todo.simple_todo import Task, ToDoApp


def test_task_creation():
    task = Task("Test task", False)
    assert task.title == "Test task"
    assert task.completed == False


def test_task_to_dict():
    task = Task("Test task", True)
    task_dict = task.parse_to_dict()
    assert task_dict == {"title": "Test task", "completed": True}


def test_todoapp_add_task():
    app = ToDoApp()
    app.clear_tasks()

    task = Task("Test task")
    app.add_task(task)

    assert len(app.tasks) == 1
    assert app.tasks[0] == task


def test_todoapp_remove_task():
    app = ToDoApp()
    app.clear_tasks()

    task1 = Task("Task 1")
    task2 = Task("Task 2")
    app.add_task(task1)
    app.add_task(task2)
    app.remove_task(1)

    assert len(app.tasks) == 1
    assert app.tasks[0] == task2


def test_todoapp_complete_task():
    app = ToDoApp()
    app.clear_tasks()

    task = Task("Test task")
    app.add_task(task)
    app.complete_task(1)

    assert app.tasks[0].completed == True


def test_todoapp_save_load_tasks():
    app = ToDoApp()
    app.clear_tasks()

    task1 = Task("Task 1", True)
    task2 = Task("Task 2", False)
    app.add_task(task1)
    app.add_task(task2)

    # Use tmp_path to create a temporary file for testing
    app.JSON_NAME = "test_tasks.json"  # type: ignore
    app.save_tasks_json()
    app2 = ToDoApp()
    app2.JSON_NAME = "test_tasks.json"  # type: ignore
    loaded_tasks = app2.load_tasks()

    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].title == "Task 1"
    assert loaded_tasks[0].completed == True
    assert loaded_tasks[1].title == "Task 2"
    assert loaded_tasks[1].completed == False
