# Nested computation of Cartesian-product of dice rolls
import itertools
results = [sum(x) for x in itertools.product(range(1,5),repeat=9)]
