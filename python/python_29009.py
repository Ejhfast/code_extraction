# Python MySQLdb cursor.execute() insert with varying number of values
placeholders = ','.join('%s' for col in columns)
query_string = "INSERT INTO `{}` {} VALUES ({})".format(table, columns, placeholders)
query.execute(query_string, values)
