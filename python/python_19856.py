# Python Celery - How to call celery tasks inside other task
celery.current_app.send_task('mymodel.tasks.mytask', args=[arg1, arg2, arg3])
