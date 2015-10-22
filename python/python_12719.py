# How to trim white space in MySQLdb using python
cursor.execute("INSERT INTO registrants VALUES( " + "'" + first_name.strip() + "'" + ", " + "'" + last_name.strip() + "'" + ");")
