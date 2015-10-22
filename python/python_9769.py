# Python sorted with list of alpha-numeric strings?
def sortqns(qnlist):
    return sorted(qnlist, key = lambda x: (len(x), x))
