# psycopg2 TypeError: not all arguments converted during string formatting
cursor.execute("""SELECT name FROM %s.customer WHERE firm_id=%%s""" % schema, each['id'])
