# Sorting a dictionary by value then key
&gt;&gt;&gt; [v[0] for v in sorted(d.iteritems(), key=lambda(k, v): (-v, k))]
['peach', 'banana', 'beetroot', 'almond', 'apple']
