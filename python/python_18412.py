# how do I make a list into multiple lists of that list?
&gt;&gt;&gt; [my_list[i:i+3] for i in xrange(0, len(my_list), 3)]
[['a', 'b', 'c'], ['d', 'e', 'f']]
