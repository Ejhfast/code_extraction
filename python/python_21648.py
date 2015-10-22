# Fetch the last row of a cursor with SQLite
cursor.execute("SELECT * FROM table ORDER BY id DESC LIMIT 1")
result = cursor.fetchone()
