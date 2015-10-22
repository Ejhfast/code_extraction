# Use 'paths' to access different levels of nested dictionaries
def nested_getter(d, keys):
    return reduce(dict.get, keys, d)
