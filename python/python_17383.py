# sqlite3 doesn't show results
cursor.execute('SELECT %s FROM song WHERE title = ? AND artist = ?' % (query),
               (title, artist))
