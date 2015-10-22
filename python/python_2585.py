# How do I get the ID of an object after persisting it in PyMongo?
doc_id = db.test.insert({"foo": 1})
db.test.remove(doc_id)
