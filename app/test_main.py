from fastapi.testclient import TestClient
from .main import app
from .main import Task

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {
        "result": []
    }

def test_create_task():
    task = Task(name="買晚餐")
    response = client.post("/task", json=task.dict())
    assert response.status_code == 201
    assert response.json() == {
        "result": {
            "id": 1,
            "name": "買晚餐",
            "status": 0
        }
    }

def test_update_task():
    task = Task(name="買早餐", status=1, id=1)
    response = client.put("/task/1", json=task.dict())
    assert response.status_code == 200
    assert response.json() == {
        "result": {
            "id": 1,
            "name": "買早餐",
            "status": 1
        }
    }

def test_update_task():
    task = Task(name="買早餐", status=1, id=2)
    response = client.put("/task/2", json=task.dict())
    assert response.status_code == 404

def test_delete_task():
    response = client.delete("/task/1")
    assert response.status_code == 200

