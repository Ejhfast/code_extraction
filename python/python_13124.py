# How to check the types contained in a list?
if isinstance(x, (list, tuple)) and all(isinstance(i, basestring) for i in x):
    #do whatever
