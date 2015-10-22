# Iterate through PyMongo Cursor as key-value pair
records = dict((record['_id'], record) for record in cursor)
