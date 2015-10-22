# Python sqlite3 error about number of bindings supplied
cur.execute("SELECT * FROM users WHERE name=?", (name,))
