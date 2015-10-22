# close() or join() equivalent for celery jobs (python)?
from celery.task.control import discard_all
discard_all()
