# No module named flask while running uWSGI
uwsgi --http-socket :3031 --plugin python --wsgi-file myflaskapp.py --callable app -H /path/to/virtualenv
