# tests/test_services.py
import pytest
from app.services import TodoService

def test_create_task_success():
    svc = TodoService()
    task = svc.create_task("Buy milk")
    assert task["id"] == 1
    assert task["title"] == "Buy milk"
    assert task["done"] is False
    assert len(svc.list_tasks()) == 1

def test_create_task_empty_title():
    svc = TodoService()
    with pytest.raises(ValueError):
        svc.create_task("")

def test_create_task_whitespace_only():
    svc = TodoService()
    with pytest.raises(ValueError):
        svc.create_task("   ")

def test_list_tasks_empty():
    svc = TodoService()
    assert svc.list_tasks() == []

def test_list_tasks_multiple():
    svc = TodoService()
    svc.create_task("Task 1")
    svc.create_task("Task 2")
    tasks = svc.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Task 1"
    assert tasks[1]["title"] == "Task 2"

def test_mark_done_sets_flag():
    svc = TodoService()
    t = svc.create_task("Task")
    svc.mark_done(t["id"])
    assert svc.list_tasks()[0]["done"] is True

def test_mark_done_non_existent():
    svc = TodoService()
    with pytest.raises(KeyError):
        svc.mark_done(999)

def test_update_task_changes_title():
    svc = TodoService()
    t = svc.create_task("Old")
    updated = svc.update_task(t["id"], "New")
    assert updated["title"] == "New"
    assert svc.list_tasks()[0]["title"] == "New"

def test_update_task_empty_title():
    svc = TodoService()
    t = svc.create_task("Task")
    with pytest.raises(ValueError):
        svc.update_task(t["id"], "")

def test_update_task_non_existent():
    svc = TodoService()
    with pytest.raises(KeyError):
        svc.update_task(999, "New Title")

def test_delete_task_removes_it():
    svc = TodoService()
    t = svc.create_task("to delete")
    svc.delete_task(t["id"])
    assert len(svc.list_tasks()) == 0

def test_delete_task_non_existent():
    svc = TodoService()
    with pytest.raises(KeyError):
        svc.delete_task(999)

def test_task_ids_increment():
    svc = TodoService()
    t1 = svc.create_task("Task 1")
    t2 = svc.create_task("Task 2")
    t3 = svc.create_task("Task 3")
    assert t1["id"] == 1
    assert t2["id"] == 2
    assert t3["id"] == 3

def test_multiple_operations_work_together():
    svc = TodoService()
    # Create multiple tasks
    t1 = svc.create_task("Task 1")
    t2 = svc.create_task("Task 2")
    t3 = svc.create_task("Task 3")
    
    # Mark one as done
    svc.mark_done(t2["id"])
    assert svc.list_tasks()[1]["done"] is True
    
    # Update one
    svc.update_task(t1["id"], "Updated Task 1")
    assert svc.list_tasks()[0]["title"] == "Updated Task 1"
    
    # Delete one
    svc.delete_task(t3["id"])
    assert len(svc.list_tasks()) == 2
    assert svc.list_tasks()[0]["title"] == "Updated Task 1"
    assert svc.list_tasks()[1]["title"] == "Task 2"

