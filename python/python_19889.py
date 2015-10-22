# How to use ndb in App Engine to query all entities of a kind with a certain value in the key pairs?
result = AClass.query(ancestor=ndb.Key(AClass,a_string))
