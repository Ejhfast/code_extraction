# Celery tries to connect to the wrong broker
celery = Celery('task', broker='redis://127.0.0.1:6379')
celery.config_from_object(celeryconfig)
