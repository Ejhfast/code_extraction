# Is there a way to run a saved SQL query from Python (using cx_Oracle)?
query = open('foo.sql', 'r').read()
cursor.execute(query)
