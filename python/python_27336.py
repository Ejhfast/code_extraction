# Celery logs on Heroku
celeryd: celery -A app.celery worker -E -B --loglevel=INFO
