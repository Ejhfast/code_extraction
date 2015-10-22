# Convert MySQLdb.fetchall() result (strings inside tuples inside tuples) to a dictionary
&gt;&gt;&gt; t = (('oranges',), ('apples',), ('pears',)
&gt;&gt;&gt; dict((item[0], None) for item in t)
{'pears': None, 'apples': None, 'oranges': None}
