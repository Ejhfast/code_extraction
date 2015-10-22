# Slicing a dictionary by keys that start with a certain string
def slicedict(d, s):
    return {k:v for k,v in d.iteritems() if k.startswith(s)}
