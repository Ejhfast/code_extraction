# wsgi application is using an older python version
pip install gunicorn
gunicorn --workers=2 /home/myapp/env/pyramid.wsgi:app
