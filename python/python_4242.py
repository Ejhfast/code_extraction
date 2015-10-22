# One-line expression to map dictionary to another
d = dict((m.get(k, k), v) for (k, v) in d.items())
