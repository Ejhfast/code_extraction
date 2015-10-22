# How to get dictionary objects from a list of tuple objects?
dict(sorted(x,key=lambda k:isinstance(k,int),reverse=True) for x in z)
Out[33]: {12: u'11:22:33:44:54:ce', 33: u'11:22:33:44:55:ff'}
