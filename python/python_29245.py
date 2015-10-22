# psycopg2 cursor.execute() pass in variable table names and items
SQL1 = 'SELECT * FROM %s' %table_name
SQL2 = SQL1+' WHERE created_on &lt; date (%s);'
cursor.execute(SQL2, (time_from, ))
