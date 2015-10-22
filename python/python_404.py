# join list of lists in python
import itertools
a = [["a","b"], ["c"]]
print list(itertools.chain(*a))
