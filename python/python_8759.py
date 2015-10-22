# Python: using map() without lambdas on a multidimensional array/list
import operator,functools
a = map(functools.partial(map, functools.partial(operator.or_, b)), a)
