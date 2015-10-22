# Escaping chars in Python and sqlite
c.execute("UPDATE movies SET rating = ? WHERE name = ?", (8.7, "'Allo 'Allo! (1982)"))
