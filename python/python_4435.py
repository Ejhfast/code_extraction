# Look up a tuple in a python dictionary matching (x,y) or (y,x)
d = {frozenset((1,2)): "foo"}
print d.get(frozenset((2,1)))
