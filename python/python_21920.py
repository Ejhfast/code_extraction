# Python and SQlite
data = conn.execute("SELECT cost from test where name like 'fish'").fetchall()
