# Programming Error in python, How do I parse values of a tuple in a table with SQL query?
insert_sql = 'INSERT INTO admin_details(username, password)  VALUES("{0}","{1}")'.format(*tup)
cur.execute(insert_sql)
conn.commit()
