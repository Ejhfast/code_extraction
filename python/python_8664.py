# How to construct a list of grouped item based on another list in python?
def group(l, window, size):
    return [l[index:index + size] for index in xrange(0, len(l) - 1, window)]
