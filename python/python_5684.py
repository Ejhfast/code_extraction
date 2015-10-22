# Make Python Sublists from a list using a Separator
&gt;&gt;&gt; [list(x[1]) for x in itertools.groupby(['|', u'MOM', u'DAD', '|', u'GRAND', '|', u'MOM', u'MAX', u'JULES', '|'], lambda x: x=='|') if not x[0]]
[[u'MOM', u'DAD'], [u'GRAND'], [u'MOM', u'MAX', u'JULES']]
