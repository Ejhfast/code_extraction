# how to clean dict values ( u'variables') in python?
&gt;&gt;&gt; {str(k): str(v[0]) for k,v in t.iteritems() if k.startswith('extra_')}
{'extra_charged': '200.0', 'extra_test1': 'jknj', 'extra_test2': 'jnjl'}
