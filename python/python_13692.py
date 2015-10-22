# Applying a list of functions to a single variable
filters = (_filter1, _filter2, _filter3)
list_after = filter(lambda x: all(f(x) for f in filters), your_list)
