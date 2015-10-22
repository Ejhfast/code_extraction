# How can I trigger tasks from another task in Python Celery?
celery.execute.send_task("task.fqn", args=[], kwargs={})
