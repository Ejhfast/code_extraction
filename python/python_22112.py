# How to pass variable for dropping table execution in Python's MySQLdb
cursor.execute("drop table if exists %s" % mdb.escape_string(table_name))
