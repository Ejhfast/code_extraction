# How to filter more than one property in Google AppEngine? (python)
foo = something.query(ndb.query.AND(something.a==5, something.b&lt;8, ndb.query.OR(something.c==1, something.c==2)))
