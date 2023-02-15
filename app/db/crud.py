from app.db.base import AppCRUD
from app.models.task import TaskOrm
from app.schemas.task import Task, TaskBase


class TaskCRUD(AppCRUD):
    def get_tasks(self) -> list[TaskOrm]:
        tasks = self.db.query(TaskOrm).all()
        return tasks

    def create_task(self, task: TaskBase) -> TaskOrm:
        taskobj = TaskOrm(**task.dict())
        self.db.add(taskobj)
        self.db.commit()
        self.db.refresh(taskobj)
        return taskobj

    def update_task(self, task_id: int, task: Task) -> TaskOrm:
        res = self.db.query(TaskOrm).filter(TaskOrm.id == task_id).update(task.dict())
        self.db.commit()
        if res:
            return TaskOrm(id=task_id, name=task.name, status=task.status)
        return None
    
    def delete_task(self, task_id: int) -> int:
        res = self.db.query(TaskOrm).filter(TaskOrm.id == task_id).delete()
        self.db.commit()
        if res:
            return res
        return None