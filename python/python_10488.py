# Extract all keys from a list of dictionaries
all_keys = set().union(*(d.keys() for d in mylist))
