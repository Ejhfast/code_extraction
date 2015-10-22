# couchdb-python and map function ViewField execute
for row in db.query(Person.by_name.map_fun):
    print row.key
