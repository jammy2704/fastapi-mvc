from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    status: int = 0  # 0: Incomplet (default), 1: Complete

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int


class TaskResponse(BaseModel):
    result: Task


class TasksResponse(BaseModel):
    result: list[Task]
