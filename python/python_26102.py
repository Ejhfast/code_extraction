# Celery workers to process the same queue, names?
$ celery -A proj worker --loglevel=INFO --concurrency=10 -n worker1.%h
$ celery -A proj worker --loglevel=INFO --concurrency=10 -n worker2.%h
$ celery -A proj worker --loglevel=INFO --concurrency=10 -n worker3.%h
