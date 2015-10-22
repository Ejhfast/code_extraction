# Is it possible to have multi-value field in Google App Engine Datastore?
class MyModel(ndb.Model):
category = ndb.StringProperty(repeated=True)
