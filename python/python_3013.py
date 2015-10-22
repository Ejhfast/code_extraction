# How to sum dict elements
dictf = reduce(lambda x, y: dict((k, v + y[k]) for k, v in x.iteritems()), dict1)
