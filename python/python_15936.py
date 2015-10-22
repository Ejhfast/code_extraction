# Create a list from a tuple of tuples
&gt;&gt;&gt; x = (('a',1), (2,3), (4,))
&gt;&gt;&gt; [str(item[0]) for item in x if item and item[0]]
['a', '2', '4']
