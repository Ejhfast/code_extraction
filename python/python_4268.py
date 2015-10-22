# Python and sqlite3 - importing and exporting databases
sql = f.read() # watch out for built-in `str`
cur.executescript(sql)
