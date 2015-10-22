# python and cx_Oracle - dynamic cursor.setinputsizes
db_types = (d[1] for d in db1_cursor.description)
db2_cursor.setinputsizes(*db_types)
