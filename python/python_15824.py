# What is the best way to convert a SymPy matrix to a numpy array/matrix
from sympy import lambdify
g_func = lambdify( (x), g )
