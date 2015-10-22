# MySQL syntax error in python but working in MySQL shell
query = "select field3,field4 from " + atable + " where field2 = %s"
cur.execute(query, (avalue,))
temp = cur.fetchall()
