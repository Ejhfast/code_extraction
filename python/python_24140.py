# Can a Celery task's definition and implementation be split?
sig = celery_app.signature('myapp.add_numbers', args=(1,2))
sig.delay()
