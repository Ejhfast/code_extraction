# python convert list to dictionary
d = dict(itertools.izip_longest(*[iter(l)] * 2, fillvalue=""))
