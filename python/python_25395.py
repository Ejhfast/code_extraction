# Celery revocations are lost on rabbitMQ restart
$ celery -A proj worker -l info --statedb=/var/run/celery/worker.state
