# Image upload to MYSQL using Google App Engine (Python)
from google.appengine.api import rdbms
conn = rdbms.connect(instance='instance_name', database='database', user='user', password='password')
