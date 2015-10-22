# More efficient way of transforming items in a list
&gt;&gt;&gt; info[:3] + [''.join(e) for e in zip(info[3::2],info[4::2])] + info[-1:]
[u'1', u'be/4', u'root', u'0.00B', u'0.00B', u'0.00%', u'0.00%', u'init']
