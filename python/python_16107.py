# MySQL and Python execution() only takes 3 arguments, 4 given
xpcounter = "UPDATE CharactersDB SET Exp=%s WHERE %s"
cur.execute(xpcounter, (xp, name,))
