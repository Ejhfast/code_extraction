# Non-sequential substitution in SymPy
Why can't I assign an arbitrary iterable to an extended slice whose step is -1?
u = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
u[0:8:3] = [ 10, 11 ]
