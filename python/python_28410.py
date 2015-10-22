# Trouble passing in variable for column name in mySQLDB for python
cmd = 'UPDATE SQLDATABASE SET ' + field + ' = %s WHERE file_name'\
      ' = %s AND slides_name = %s;'
cur.execute(cmd, (temp_list[y],filename,temp_list[0]))
