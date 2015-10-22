# How to get variable length placeholders in a Python call to SQLite3
tup = ... # some sequence/tuple of unknown length
sql = 'SELECT * FROM table WHERE word IN (%s)' % ', '.join('?' for a in tup)
c.execute(sql, tup)
