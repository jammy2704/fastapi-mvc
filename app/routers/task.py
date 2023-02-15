from fastapi import APIRouter, Depends, status

from app.db.database import get_db
from app.schemas.task import Task, TaskBase, TaskResponse, TasksResponse
from app.services.task import TaskService
from app.utils.service_result import append_response_format, handle_result

router = APIRouter(
    tags=["tasks"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@router.get("/tasks", response_model=TasksResponse)
async def get_task(db: get_db = Depends()):
    tasks = TaskService(db).get_tasks()
    return append_response_format(handle_result(tasks))


@router.post("/task", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskBase, db: get_db = Depends()):
    result = TaskService(db).create_task(task)
    return append_response_format(handle_result(result))


@router.put("/task/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: Task, db: get_db = Depends()):
    result = TaskService(db).update_task(task_id, task)
    return append_response_format(handle_result(result))


@router.delete("/task/{task_id}", response_model=None)
async def delete_task(task_id: int, db: get_db = Depends()):
    result = TaskService(db).delete_task(task_id)
    return handle_result(result)
