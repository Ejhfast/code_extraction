# More efficient way to remove items from large data sets
def remaining(ls, y, z):
    diff = y.difference(z)
    return filter(lambda i: i[0] in diff, ls)
