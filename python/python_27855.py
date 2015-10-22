# Loss of quotes when encoding into ascii
How to do IN query with a python tuple
sql_stmt = 'SELECT * FROM peoples WHERE person IN (%s)' % ','.join(map(str,people))
