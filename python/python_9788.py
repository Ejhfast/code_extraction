# Evaluate sympy expression from an array of values
from sympy.utilities.lambdify import lambdify
func = lambdify(x, big_expression_containing_x,'numpy') # returns a numpy-ready function
numpy_array_of_results = func(numpy_array_of_arguments)
