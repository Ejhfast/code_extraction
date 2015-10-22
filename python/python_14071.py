# Sort a dict by numeric value of dict.values
&gt;&gt;&gt; d = {'a': '1', 'c': '10', 'b': '8', 'e': '11', 'g': '3', 'f': '2'}
&gt;&gt;&gt; sorted(d, key=lambda i: int(d[i]))
['a', 'f', 'g', 'b', 'c', 'e']
