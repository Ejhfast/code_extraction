# How to configure Django database using Heroku?
DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ATOMIC_REQUESTS'] = True
