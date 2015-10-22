# Extract from last element of a list to a certain string
&gt;&gt;&gt; list_char = ['a','b','c','s','a','d','g','b','e']
&gt;&gt;&gt; list_char[-list_char[::-1].index('s')-1:]
['s', 'a', 'd', 'g', 'b', 'e']
