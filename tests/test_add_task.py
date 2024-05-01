import pytest
from Task import Task
from TaskPoolAction import TasksPoolAction

def test_add_task():
    task_pool = TasksPoolAction()
    task_name = "Go to the gym"
    category = "Health"
    due_date = "2024-03-25"
    priority = "High"
    task = Task(task_name, category, due_date, priority)
    task_pool.add_task(task)
    assert len(task_pool.pending_tasks) == 1
    assert task_pool.pending_tasks[0].task_name == task_name
    assert task_pool.pending_tasks[0].category == category
    assert task_pool.pending_tasks[0].due_date == due_date
    assert task_pool.pending_tasks[0].priority == priority
    task_pool2 = TasksPoolAction()
    task_pool2.add_task(task)
    assert len(task_pool2.pending_tasks) == 1
    assert task_pool2.pending_tasks[0].task_name == task_name
    assert task_pool2.pending_tasks[0].category == category
    assert task_pool2.pending_tasks[0].due_date == due_date
    assert task_pool2.pending_tasks[0].priority == priority