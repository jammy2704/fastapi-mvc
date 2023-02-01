# Gogolook task

default port is 80

Please find the openapi doc at http://localhost/docs .

The postman collection is available at [collection](Gogolook.postman_collection.json).

## Unit test
Just type ```pytest```

```
(gogolook) jimmyhuang@windows:~/gogolook_task$ pytest -vv
============================================================= test session starts ==============================================================
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0 -- /home/jimmyhuang/.pyenv/versions/gogolook/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/jimmyhuang/gogolook_task
plugins: anyio-3.6.2
collected 4 items

app/test_main.py::test_get_tasks PASSED                                                                                                  [ 25%]
app/test_main.py::test_create_task PASSED                                                                                                [ 50%]
app/test_main.py::test_update_task PASSED                                                                                                [ 75%]
app/test_main.py::test_delete_task PASSED                                                                                                [100%]

============================================================== 4 passed in 0.31s ===============================================================
(gogolook) jimmyhuang@windows:~/gogolook_task$
```
