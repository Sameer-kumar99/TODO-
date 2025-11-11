# tests/test_app.py
"""
Integration tests for the Flask API endpoints.
These tests verify the API behaves correctly from an external perspective.
"""

def test_create_task_endpoint(client):
    resp = client.post("/tasks", json={"title": "API Task"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "API Task"
    assert data["done"] is False
    assert "id" in data

def test_create_task_invalid(client):
    resp = client.post("/tasks", json={"title": ""})
    assert resp.status_code == 400
    data = resp.get_json()
    assert "error" in data
    assert "Title is required" in data["error"]

def test_create_task_missing_title(client):
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400

def test_list_tasks_endpoint(client):
    client.post("/tasks", json={"title": "First"})
    resp = client.get("/tasks")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "First"

def test_list_tasks_empty(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_mark_done_endpoint(client):
    # Create a task
    create_resp = client.post("/tasks", json={"title": "Task to complete"})
    task_id = create_resp.get_json()["id"]
    
    # Mark as done
    resp = client.post(f"/tasks/{task_id}/done")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["done"] is True
    
    # Verify in list
    list_resp = client.get("/tasks")
    tasks = list_resp.get_json()
    task = next((t for t in tasks if t["id"] == task_id), None)
    assert task is not None
    assert task["done"] is True

def test_mark_done_non_existent(client):
    resp = client.post("/tasks/999/done")
    assert resp.status_code == 404
    data = resp.get_json()
    assert "error" in data

def test_update_task_endpoint(client):
    # Create a task
    create_resp = client.post("/tasks", json={"title": "Original Title"})
    task_id = create_resp.get_json()["id"]
    
    # Update the task
    resp = client.put(f"/tasks/{task_id}", json={"title": "Updated Title"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["title"] == "Updated Title"
    
    # Verify in list
    list_resp = client.get("/tasks")
    tasks = list_resp.get_json()
    task = next((t for t in tasks if t["id"] == task_id), None)
    assert task is not None
    assert task["title"] == "Updated Title"

def test_update_task_empty_title(client):
    create_resp = client.post("/tasks", json={"title": "Task"})
    task_id = create_resp.get_json()["id"]
    
    resp = client.put(f"/tasks/{task_id}", json={"title": ""})
    assert resp.status_code == 400
    data = resp.get_json()
    assert "error" in data

def test_update_task_non_existent(client):
    resp = client.put("/tasks/999", json={"title": "New Title"})
    assert resp.status_code == 400
    data = resp.get_json()
    assert "error" in data

def test_delete_task_endpoint(client):
    # Create a task
    create_resp = client.post("/tasks", json={"title": "Task to delete"})
    task_id = create_resp.get_json()["id"]
    
    # Delete the task
    resp = client.delete(f"/tasks/{task_id}")
    assert resp.status_code == 204
    
    # Verify it's gone
    list_resp = client.get("/tasks")
    tasks = list_resp.get_json()
    task = next((t for t in tasks if t["id"] == task_id), None)
    assert task is None

def test_delete_task_non_existent(client):
    resp = client.delete("/tasks/999")
    assert resp.status_code == 404
    data = resp.get_json()
    assert "error" in data

def test_full_crud_workflow(client):
    # Create multiple tasks
    t1_resp = client.post("/tasks", json={"title": "Task 1"})
    t2_resp = client.post("/tasks", json={"title": "Task 2"})
    t1_id = t1_resp.get_json()["id"]
    t2_id = t2_resp.get_json()["id"]
    
    # List tasks
    list_resp = client.get("/tasks")
    tasks = list_resp.get_json()
    assert len(tasks) == 2
    assert len([t for t in tasks if t["id"] in [t1_id, t2_id]]) == 2
    
    # Update task 1
    client.put(f"/tasks/{t1_id}", json={"title": "Updated Task 1"})
    
    # Mark task 2 as done
    client.post(f"/tasks/{t2_id}/done")
    
    # Verify updates
    list_resp = client.get("/tasks")
    tasks = list_resp.get_json()
    t1 = next((t for t in tasks if t["id"] == t1_id), None)
    t2 = next((t for t in tasks if t["id"] == t2_id), None)
    assert t1["title"] == "Updated Task 1"
    assert t2["done"] is True
    
    # Delete task 1
    client.delete(f"/tasks/{t1_id}")
    
    # Verify deletion
    list_resp = client.get("/tasks")
    tasks = list_resp.get_json()
    assert len(tasks) == 1
    assert next((t for t in tasks if t["id"] == t1_id), None) is None
    assert next((t for t in tasks if t["id"] == t2_id), None) is not None

