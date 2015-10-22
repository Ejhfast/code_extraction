# Formatting sql %like%
sql = "select count(*) from video where territories like %s"
cursor.execute(sql, ('%' + territory + '%',))
