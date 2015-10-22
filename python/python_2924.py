# Do I reference the session when making any db calls in sqlalchemy?
query = users.select()
result = conn.execute(query)
