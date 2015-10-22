# Python: Check if one dictionary is a subset of another larger dictionary
all(item in superset.items() for item in subset.items())
