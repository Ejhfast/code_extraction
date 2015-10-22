# Python MySQLdb WHERE SQL LIKE
c.execute("SELECT * FROM data WHERE params LIKE %s LIMIT 1", ("%" + param + "%",))
