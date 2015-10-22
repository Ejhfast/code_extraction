# App Engine Python NDB Equivalent to Java's @NotPersistent
class Person(ndb.model):
        name = StringProperty()
        _helper_var = 5
