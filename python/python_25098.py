# Inserting multi-word string and an empty array with psycopg2
cur.execute("""INSERT INTO items (name, description, sizes) VALUES (%s, %s, %s)""", (name, description, sizes))
