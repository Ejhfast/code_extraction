# MySQL syntax error using python to add column to a table
query = "ALTER TABLE segment_table ADD %s VARCHAR(40)" % (key)
cursor.execute( query )
