import pytest
import os
from task_manager import TaskManager

def test_add_and_complete_task():
    task_manager = TaskManager()
    task_manager.add_task("Task 1")
    task_manager.complete_task(0)
    assert task_manager.tasks[0]["completed"] is True


def test_remove_task():
    task_manager = TaskManager()
    task_manager.add_task("Task 1")
    task_manager.add_task("Task 2")
    task_manager.remove_task(0)
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0]["description"] == "Task 2"


def test_save_and_load_tasks(tmp_path):
    task_manager = TaskManager()
    filename = tmp_path / "tasks.json"
    task_manager.add_task("Task 1")
    task_manager.add_task("Task 2")
    task_manager.save_to_json(filename)

    new_task_manager = TaskManager()
    new_task_manager.load_from_json(filename)
    assert len(new_task_manager.tasks) == 2
    assert new_task_manager.tasks[0]["description"] == "Task 1"
    assert new_task_manager.tasks[1]["description"] == "Task 2"