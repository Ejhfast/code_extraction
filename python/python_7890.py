# Running a Celery task when unable to import that task
send_task("tasks.test_task", task_id=task_id, queue=queue)
