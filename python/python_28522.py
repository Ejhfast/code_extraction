# Correct python code to insert NULL value into MySQL
cur.execute("INSERT INTO name (first, middle, last) VALUES (%s, %s, %s)", (f, m, l))
