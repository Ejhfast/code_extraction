# Sort dictionary with tuple values and filter top k elements
In [1]: from collections import OrderedDict
In [2]: OrderedDict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=False)[:k])
Out[2]: OrderedDict([('b', (1, 2)), ('a', (3, 4)), ('c', (10, 11))])
