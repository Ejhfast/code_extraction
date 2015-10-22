# Sql-statement with variables in python
cursor.execute("UPDATE setting set foo=%s WHERE bar=%s", (4, str(sys.argv[1])))
