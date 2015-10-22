# Python: Modified sorting order for a list
&gt;&gt;&gt; items = ['24/2', '24/3', '25/2', '6']
&gt;&gt;&gt; sorted(items, key=lambda s: [int(n) for n in s.split('/')])
['6', '24/2', '24/3', '25/2']
