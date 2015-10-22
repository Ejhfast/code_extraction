# How to traverse a query result in python?
for row in c.execute('SELECT * from table if time = "14:00:00"').fetchall():
    print row
