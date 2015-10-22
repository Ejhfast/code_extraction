# looping over list of lists without nesting too much
from itertools import product
for i,j in product(range(len(a)), repeat=2):
    ...
