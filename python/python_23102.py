# How to On Duplicate Key Update
cur.execute(""" INSERT INTO logs (1, 2, 3) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE 1=%s, 3=%s """, (line[0], line[1], line[2], line[0], line[2]))
