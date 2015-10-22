# Finding mismatched item for same index in a python list
missing = [b for a,b in itertools.izip_longest(l1,l2,fillvalue=object()) if a != b]
