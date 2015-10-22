# how to add all of these values in a python dictionary
&gt;&gt;&gt; x = {0: {'count': 1000}, 1: {'count': 2000}}
&gt;&gt;&gt; sum(v['count'] for v in x.values())
3000
