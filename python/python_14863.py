# Celery is not working on my Heroku
from apps.otgcelery.tasks import add
result = add.delay(2,2)
