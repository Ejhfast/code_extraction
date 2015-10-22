# Python: Make new tuple by attaching info from existing list
result = tuple(itertools.izip_longest(l, (x[1] for x in f for y in range(x[0])), fillvalue='None'))
