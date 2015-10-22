# celery task doesn't return result to client
celery -A celery_test.service worker --loglevel=debug --pool=solo
