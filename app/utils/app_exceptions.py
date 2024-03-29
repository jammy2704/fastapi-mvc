from fastapi import Request, status
from starlette.responses import JSONResponse


class AppExceptionCase(Exception):
    def __init__(self, status_code: int, context: dict):
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.context = context

    def __str__(self):
        return (
            f"<AppException {self.exception_case} - "
            + f"status_code={self.status_code} - context={self.context}>"
        )


async def app_exception_handler(request: Request, exc: AppExceptionCase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "app_exception": exc.exception_case,
            "context": exc.context,
        },
    )


class AppException():
    class TaskCreateFail(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Task creation failed
            """
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            AppExceptionCase.__init__(self, status_code, context)

    class TaskNotExist(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Task not found
            """
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(self, status_code, context)
