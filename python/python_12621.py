# CSV export in Stream (from Django admin on Heroku)
web: gunicorn myapp.wsgi -b 0.0.0.0:$PORT --timeout 600
celeryd: python manage.py celeryd -E -B --loglevel=INFO
