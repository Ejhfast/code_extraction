# Minimizing a function with scipy.optimize parallely with ipython
def root(b):
    g = lambda a, b=b : f(a,b)
    return scipy.optimize.fsolve( g, 0.0 )
