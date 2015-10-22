# Run Django project inside wordpress (on suburl of wordpress using Apache and mod_wsgi)
ServerName wptesting.com
WSGIScriptAlias /django /path_to/wsgi.py
