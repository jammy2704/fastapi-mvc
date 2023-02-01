from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

app = FastAPI()

tasks_in_memory = []
id = 0

class Task(BaseModel):
    id: int = 0
    name: str
    status: int = 0  # 0: Incomplet (default), 1: Complete

@app.get("/tasks")
async def list_tasks():
    return {"result": tasks_in_memory}

@app.post("/task", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    global id
    id += 1
    task.id = id
    tasks_in_memory.append(task)
    return {"result": task}

@app.put("/task/{id}")
async def update_task(id: int, task: Task):
    i = next((i for i, task in enumerate(tasks_in_memory) if task.id == id), None)
    if i == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task id not found")
    tasks_in_memory[i] = task
    return {"result": task}

@app.delete("/task/{id}")
async def delete_task(id: int):
    i = next((i for i, task in enumerate(tasks_in_memory) if task.id == id), None)
    if i == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task id not found")
    del tasks_in_memory[i]
