# Retrieve a task result object, given a `task_id` in Celery
result = MyTask.AsyncResult(task_id)
result.get()
