# How can I add a column with mySQLdb in python?
query = "ALTER TABLE upload ADD %s INT(15)" % (colName)
c.execute( query )
