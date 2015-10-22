# How to retrieve from python dict where key is only partially known?
value = next(v for (k,v) in some_dict.iteritems() if 'substring' in k)
