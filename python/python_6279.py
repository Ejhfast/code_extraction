# How to slice list into contiguous groups of non-zero integers in Python
import itertools
[ list(x[1]) for x in itertools.groupby(data, lambda x: x == 0) if not x[0] ]
