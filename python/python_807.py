# convert string to dict using list comprehension in python
&gt;&gt;&gt; dict( (n,int(v)) for n,v in (a.split('=') for a in string.split() ) )
{'a': 0, 'c': 3, 'b': 1}
