# Encode Python list to UTF-8
&gt;&gt;&gt; items =  [u'a', u'b', u'c']
&gt;&gt;&gt; [x.encode('utf-8') for x in items]
['a', 'b', 'c']
