# sqlite3.OperationalError: no such column. But that's not a column
curs.execute("SELECT * FROM tracks WHERE ISRC = ?", (line[8],))
