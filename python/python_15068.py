# Python : parse string to sub string for searching
&gt;&gt;&gt; strs= "Hello world"
&gt;&gt;&gt; [y for x in strs.split() for y in (x[:i] for i in  xrange(2,len(x)+1)) ]
['He', 'Hel', 'Hell', 'Hello', 'wo', 'wor', 'worl', 'world']
