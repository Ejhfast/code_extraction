# Converting a list of strings, into a list of tuples containing integers
&gt;&gt;&gt; L = [' 1 2 ', '3 4 ']
&gt;&gt;&gt; [tuple(int(y) for y in x.split()) for x in L]
[(1, 2), (3, 4)]
