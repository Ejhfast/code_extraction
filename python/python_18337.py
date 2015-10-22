# python sqlite3: How to use LIKE and ? to do partial matching?
cursor.execute('SELECT * FROM songs WHERE filename LIKE ?', ('{}%'.format(key_string),))
