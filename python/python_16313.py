# python .count for multidimensional arrays (list of lists)
&gt;&gt;&gt; list = [['foobar', 'a', 'b'], ['x', 'c'], ['y', 'd', 'e', 'foobar'], ['z', 'f']]
&gt;&gt;&gt; sum(x.count('foobar') for x in list)
2
