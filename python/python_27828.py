# Passing iterator value to Sqlite3 like condition of select clause in python
c.execute("SELECT Plot FROM Movies WHERE Genre LIKE ? ",('%'+genre+'%',) )
