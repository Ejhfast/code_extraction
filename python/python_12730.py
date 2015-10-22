# Concatenating SQL statement strings
c = db.cursor()
values_to_insert = [("a","b"),("c","d"),...]
c.execute_many("INSERT INTO table (val1,val2) VALUES (?,?)",values_to_insert  )
