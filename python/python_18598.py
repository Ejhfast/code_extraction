# Remove all empty nested lists
def remove_empty(l):
    return tuple(filter(lambda x:not isinstance(x, (str, list, tuple)) or x, (remove_empty(x) if isinstance(x, (tuple, list)) else x for x in l)))
