# Cancel an already executing task with Celery?
&gt;&gt;&gt; from celery.task.control import revoke
&gt;&gt;&gt; revoke(task_id, terminate=True)
