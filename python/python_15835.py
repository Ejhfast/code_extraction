# Generator expression calling a function that returns lists
from itertools import chain
result = list(chain.from_iterable(foo(x) for x in arr))
