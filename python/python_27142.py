# Hardcoding values into ndb model
class DBExamplestart(Examplestart):
    variable = ndb.KeyProperty(kind=DBUser, default=ndb.Key(DBUser, 776))
    statement = ndb.StringProperty(indexed=False, default='First')
