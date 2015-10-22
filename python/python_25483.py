# How to update a column for multiple records dependant on other column values with sqlite python 2.7
c.execute("UPDATE Table1 SET Time_out = TIME('now') WHERE Time_in&lt;&gt;'' and Time_out=''")conn.commit()
