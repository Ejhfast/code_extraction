# how to check values if it has a like/same key in a dict in python?
&gt;&gt;&gt; {k: v for k,v in d.iteritems() if k.startswith('extra_')}
{u'extra_test1': [u'jknj'], u'extra_test2': [u'jnjl']}
