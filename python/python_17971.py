# Separating celery consumer and producer
from yourmodule.yourapp import celery
celery.send_task("yourtasksmodule.yourtask", args=["Hello World"])
