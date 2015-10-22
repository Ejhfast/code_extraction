# combine list of lists in python (similar to string.join but as a list comprehension?)
&gt;&gt;&gt; lis = [['A',1,2],['B',3,4]]
&gt;&gt;&gt; [', '.join(map(str, x)) for x in lis ]
['A, 1, 2', 'B, 3, 4']
