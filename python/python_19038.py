# convert list of dicts to list
&gt;&gt;&gt; fields = [{'name':'count', 'label':'Count'},{'name':'type', 'label':'Type'}]
&gt;&gt;&gt; [f['name'] for f in fields]
['count', 'type']
