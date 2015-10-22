# Lookup table for unhashable in Python
def __hash__(self):
    return hash(frozenset(self.iteritems()))
