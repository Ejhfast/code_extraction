# Cartesian product of a dictionary of lists
def my_product(dicts):
    return (dict(izip(dicts, x)) for x in product(*dicts.itervalues()))
