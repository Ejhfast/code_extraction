# Sorting strings with integer values in python
&gt;&gt;&gt; from itertools import chain
&gt;&gt;&gt; [x[1] for x in sorted(chain.from_iterable(sample_lists), key=lambda x:int(x[0]))]
[u'penguin', u'kelp', u'otter', u'clam', u'egg']
