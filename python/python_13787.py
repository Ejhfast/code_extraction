# How to use itertools to output results of only a certain length
import itertools
for tup in itertools.product(range(0x100), repeat=3):
    ...
