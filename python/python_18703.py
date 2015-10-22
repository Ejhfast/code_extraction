# Google App Engine: Creating entity categories
class Book(ndb.Model):
    title = ndb.StringProperty(required = True)
    genre = ndb.StringProperty(repeated=True)
