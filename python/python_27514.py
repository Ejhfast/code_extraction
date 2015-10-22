# Trying to create an SQLite table in Python 3 but it's saying I'm supplying too many values
cursor.executemany("INSERT INTO contacts VALUES (?,?)", list)
