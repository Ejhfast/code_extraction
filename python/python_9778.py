# full type of object in python
def full_type(obj):
    return "%r of " % type(obj) + ','.join('%r' % t for t in set([type(o) for o in obj]))
