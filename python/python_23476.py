# Python List of Strings to MySQL
subs = ','.join('%s' for _ in lst)
sql = "select * from test.db where name in ({})".format(subs)
cursor.execute(sql, tuple(subs))
