# Error encountered while using the SQL Module
c.execute(
    "INSERT INTO Class{} (Name,Score1,Score2,Score3) VALUES (?,?,?,?)".format(Class),
    (name,score1,score2,score3))
