# PostgreSQL wiht pg8000 - INSERT results from an SQL to another table
cursor.execute("INSERT INTO secondtable VALUES %s" % str(results))
