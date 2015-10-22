# How to find the number of unique elements in a list of ndarrays?
len(set([tuple(v) for v in l]))
