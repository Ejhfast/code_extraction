# How to use dj-database-url while connecting with postgresql in heroku using python
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
