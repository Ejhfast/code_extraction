# Reverse the `pairwise` generator
def unpair(iterable):
    p = iter(iterable)
    return chain(next(p, []), (x[1] for x in p))
