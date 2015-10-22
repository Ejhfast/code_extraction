# Adding spaces in elements of list(PY)
def equalize_lengths(l):
    length = len(max(l, key=len))
    return [e.ljust(length) for e in l]
