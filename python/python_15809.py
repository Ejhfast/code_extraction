# I have a dictionary with a value that is as a list of unicode strings, I would like to get them as a string?
&gt;&gt;&gt; d = {'1':[u'06'],'2':[u'02',u'03',u'05',u'10']}
&gt;&gt;&gt; print ','.join([str(u) for u in d.get('2')])
02,03,05,10
