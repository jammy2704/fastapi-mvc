from app.db.crud import TaskCRUD
from app.schemas.task import Task, TaskBase
from app.services.base import AppService
from app.utils.app_exceptions import AppException
from app.utils.service_result import ServiceResult


class TaskService(AppService):
    def get_tasks(self) -> ServiceResult:
        tasks = TaskCRUD(self.db).get_tasks()
        return ServiceResult(tasks)

    def create_task(self, task: TaskBase) -> ServiceResult:
        task = TaskCRUD(self.db).create_task(task)
        if not task:
            return ServiceResult(AppException.TaskCreateFail())
        return ServiceResult(task)

    def update_task(self, task_id: int, task: Task) -> ServiceResult:
        task = TaskCRUD(self.db).update_task(task_id, task)
        if not task:
            return ServiceResult(AppException.TaskNotExist({"task_id": task_id}))
        return ServiceResult(task)

    def delete_task(self, task_id: int) -> ServiceResult:
        res = TaskCRUD(self.db).delete_task(task_id)
        if not res:
            return ServiceResult(AppException.TaskNotExist({"task_id": task_id}))
        return ServiceResult(None)
