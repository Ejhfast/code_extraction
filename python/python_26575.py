# read value from file then pass value in sql UPDATE command(python script)
c.execute("UPDATE table1 SET waiting=%s where dept='billing'", (data.strip(),))
