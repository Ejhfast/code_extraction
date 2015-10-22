# How to get first element in a list of tuples?
&gt;&gt;&gt;a = [(1, u'abc'), (2, u'def')]
&gt;&gt;&gt;b = [int(i[0]) for i in a]
[1, 2]
