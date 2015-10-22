# How to set up Django to run tests on PostgreSQL on Travis CI?
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
