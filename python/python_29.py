# Sorting a dict on __iter__
def itersorted(d):
    for key in sorted(d):
        yield d[key]
