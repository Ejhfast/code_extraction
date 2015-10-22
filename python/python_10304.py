# Python: Map list of two-entry-dicts to dict with first entry as key and second as value
&gt;&gt;&gt; lis = [{'date': 1, 'value':5}, {'date':2,'value':3}]
&gt;&gt;&gt; {x['date']:x['value'] for x in lis}
{1: 5, 2: 3}
