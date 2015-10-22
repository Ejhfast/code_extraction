# Change text_factory in Django/sqlite
from django.db import connection
connection.connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")
