# How to delete rows from the datastore that our app uses in google appengine?
q = db.GqlQuery("SELECT * FROM Foo")
results = q.fetch(10)
db.delete(results)
