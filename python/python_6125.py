# Writing a single table value in sqlite3
cursor.execute("update records set y = ? where x = ?", (y, x))
