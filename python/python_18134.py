# python sqlite3 cursor.execute() with parameters leads to syntax error near ? (paramstyle qmark)
sql = "CREATE TABLE IF NOT EXISTS {} ( name TEXT, street TEXT, time REAL, age INTEGER )".format(*values)
