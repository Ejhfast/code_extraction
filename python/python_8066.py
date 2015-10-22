# Insert a python dict into an SQLite DB
query = 'INSERT INTO packages VALUES(%s)' % ','.join(['?'] * len(Tags))
cursor.execute(query, Tags)
