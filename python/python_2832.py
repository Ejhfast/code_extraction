# Celery - Get task id for current task
@task
def do_job(path, task_id=None):
    cache.set(task_id, operation_results)
