# Psycopg2 uses up memory on large select query
cur = conn.cursor('cursor-name') # server side cursor
cur.itersize = 10000 # how much records to buffer on a client
cur.execute("SELECT * FROM mytable;")
