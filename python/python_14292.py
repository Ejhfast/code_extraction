# Insert python binary string object in MySQL blob
query = '''INSERT INTO cheese (data) VALUES (%s)'''
cur.execute(query, (bd,))
