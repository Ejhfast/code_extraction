# how to set group=True in couchdb-python
for row in db.query(Person.by_name.map_fun, '_count', group=True):
  print row
