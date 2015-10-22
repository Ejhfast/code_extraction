# Reorder a list 'in place', according to another list
X[:] = [x for (y,x) in sorted(zip(Y,X))]
