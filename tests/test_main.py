import pytest

from app.db.crud import TaskCRUD
from app.schemas.task import TaskBase


@pytest.fixture
def add_task(db):
    TaskCRUD(db).create_task(TaskBase(name="買晚餐"))
    

def test_get_tasks(client, add_task):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {
        "result": [{'id': 1, 'name': '買晚餐', 'status': 0}]
    }


def test_create_task(client, db):
    input_task = {"name": "買晚餐"}
    response = client.post("/task", json=input_task)
    assert response.status_code == 201
    assert response.json() == {
        "result": {
            "id": 1,
            "name": "買晚餐",
            "status": 0
        }
    }
    tasts = TaskCRUD(db).get_tasks()
    assert tasts[0].to_dict() == {'id': 1, 'name': '買晚餐', 'status': 0}


def test_create_task_validation_error(client, db):
    input_task = {"namee": "買晚餐"}
    response = client.post("/task", json=input_task)
    assert response.status_code == 422


def test_update_task(client, db, add_task):
    input_task = {"name": "買早餐", "status": 1, "id": 1}
    response = client.put("/task/1", json=input_task)
    assert response.status_code == 200
    assert response.json() == {
        "result": {
            "id": 1,
            "name": "買早餐",
            "status": 1
        }
    }
    tasts = TaskCRUD(db).get_tasks()
    assert tasts[0].to_dict() == {'id': 1, 'name': '買早餐', 'status': 1}


def test_update_task_not_exists(client):
    input_task = {"name": "買早餐", "status":"1", "id":"2"}
    response = client.put("/task/2", json=input_task)
    assert response.status_code == 404


def test_delete_task(client, db, add_task):
    response = client.delete("/task/1")
    assert response.status_code == 200
    tasts = TaskCRUD(db).get_tasks()
    assert tasts == []


def test_delete_task_not_exists(client):
    response = client.delete("/task/1")
    assert response.status_code == 404
