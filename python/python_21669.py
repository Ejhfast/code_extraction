# How can I achieve converting a list to 2d list this using itertools or collections with high performance
&gt;&gt;&gt; thing = [lst[i:i+n] for i in range(0,len(lst),n)]
&gt;&gt;&gt; thing
[['a', 'b'], ['c', 2], ['e']]
