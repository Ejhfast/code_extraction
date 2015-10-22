# Python String Formats with SQL Wildcards and LIKE
sql = "SELECT column FROM table WHERE col1=%s AND col2=%s"
params = (col1_value, col2_value)
cursor.execute(sql, params)
