# How to configure Django to use Heroku Dev Postgre while local?
import dj_database_url
DATABASES['default'] =  dj_database_url.config(default='postgres://foo:bar@somehost.amazonaws.com:5432/somedb')
