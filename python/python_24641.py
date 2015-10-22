# Would like to just display 3 rows from mySQL result in python
for row in cur.fetchall()[:3]:
    print row
