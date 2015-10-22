# Elegant way to modify a list of variables by reference in Python?
for x in ['a', 'b', 'c', 'd', 'e']:
    setattr(i, x, f(getattr(i, x)))
