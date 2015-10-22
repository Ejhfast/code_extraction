# Unexpected empty results of GQL Query
class Person(db.Model):
    name = db.StringProperty()
    age = db.IntegerProperty(indexed=True)
