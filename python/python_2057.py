# Filtering by entity key name in Google App Engine on Python
from google.appengine.api.datastore import Key
query.filter("__key__ &gt;=", Key.from_path('User', 'abc'))
