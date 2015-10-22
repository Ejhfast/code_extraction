# sympy solve function as function
In [5]: x, y, z = Symbol('x'), Symbol('y'), Symbol('z')
In [6]: solve((Eq(2*y+z,1/x), Eq(2*z+y,x)),y,z)
Out[6]: {y: (-x**2 + 2)/(3*x), z: (2*x**2 - 1)/(3*x)}
