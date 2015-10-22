# Python: uniqueness in list of lists
In [11]: list(map(list, set(map(tuple, L))))
Out[11]: [[3, 4, 5], [1, 2, 3]]
