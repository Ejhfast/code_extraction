# Ignore part of a python tuple
a = (1, 2, 3, 4, 5)
idxs = [0, 3, 4]
a1, b1, c1 = (a[i] for i in idxs)
