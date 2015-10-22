# Iterating over N dimensions in Python
itertools.product(*[xrange(i, i+j) for i,j in zip(start, size)])
