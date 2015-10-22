# How can I test the validity of a ReferenceProperty in Appengine?
db.Query(keys_only=True).filter('__key__ =', test_key).count(1) == 1
