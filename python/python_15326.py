# Insert datetime.datetime object in MySQL
cursor.execute('INSERT INTO tweets (created_at) VALUES ("{created_at}")'.format(created_at=t))
