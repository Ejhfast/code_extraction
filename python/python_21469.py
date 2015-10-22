# how do I insert a row to a MySQL table in Python?
cursor.execute('INSERT INTO ' + table_name + ' (haiku_text, date_written) VALUES (%s, %s)', (haiku_text, date_written))
