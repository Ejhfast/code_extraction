# Insert lists in SQLite database
cur.executemany("INSERT INTO my_table(ID, vegetables, fruits) VALUES (?,?,?)",
    ((i, v, f) for (i, (v, f)) in enumerate(zip(vegetables, fruits), 1)))
