# execute sql command in python
cur.execute("UPDATE visitors SET nb_visits = nb_visits+1 WHERE id = 1")
db.commit()
