# adding list indexes in python
&gt;&gt;&gt; data = [['1', '1', '1', '1', '1', '.12'], ['1', '1', '1', '1', '1', '.13']]
&gt;&gt;&gt; sum(float(x[-1]) for x in data)
0.25
