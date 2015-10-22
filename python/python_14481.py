# Is any elegant way to make a list contains some integers to become a list contains some tuples?
pairs = zip(*[iter(a)]*2)
