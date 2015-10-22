# Map multiple lists of values to a list of keys in a python dictionary?
data = [dict(itertools.izip(headers, entries) for entries in values]
