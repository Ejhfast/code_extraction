# Need an easy way to remove duplicates of nested tuples in python
In [10]: set(tuple(sorted(elt)) for elt in example)
Out[10]: set([ ((0, 1), (2, 1)) ])
