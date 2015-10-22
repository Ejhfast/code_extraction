# taking intersection of N-many lists in python
def intersection(first, *others):
    return set(first).intersection(*others)
