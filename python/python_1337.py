# Get all table names in a Django app
from django.db import connection
tables = connection.introspection.table_names()
seen_models = connection.introspection.installed_models(tables)
