# Multi-database in Django
from django.db import connections
#cursor = connection.cursor()
cursor = connections['osm'].cursor()
