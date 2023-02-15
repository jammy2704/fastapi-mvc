# Fastapi-mvc task

default port is 80 (dev env is 8000)

Please find the openapi doc at http://localhost/docs .

The postman collection is available at [collection](fastapi-mvc.postman_collection.json).

## Useful cmd in Makefile
1. ```make dev``` will run service as dev mode on local
2. ```make test``` will run unit test by pytest
3. ```generate_req``` will generate compatible requirements.txt from poetry to pip for docker container

## Unit test
Just type ```make test``` under fastapi-mvc/

```
(fastapi-mvc-py3.10) jimmyhuang@windows:~/fastapi-mvc$ make test
============================================================= test session starts ==============================================================
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0 -- /home/jimmyhuang/fastapi-mvc/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/jimmyhuang/fastapi-mvc
plugins: anyio-3.6.2
collected 7 items

tests/test_main.py::test_get_tasks PASSED                                                                                                [ 14%]
tests/test_main.py::test_create_task PASSED                                                                                              [ 28%]
tests/test_main.py::test_create_task_validation_error PASSED                                                                             [ 42%]
tests/test_main.py::test_update_task PASSED                                                                                              [ 57%]
tests/test_main.py::test_update_task_not_exists PASSED                                                                                   [ 71%]
tests/test_main.py::test_delete_task PASSED                                                                                              [ 85%]
tests/test_main.py::test_delete_task_not_exists PASSED                                                                                   [100%]

============================================================== 7 passed in 0.14s ===============================================================
(fastapi-mvc-py3.10) jimmyhuang@windows:~/fastapi-mvc$
```
