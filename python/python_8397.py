# Getting the key for a value
&gt;&gt;&gt; revdict = dict([(mydict[key],key) for key in mydict])
&gt;&gt;&gt; revdict['myValue']
'myKey'
