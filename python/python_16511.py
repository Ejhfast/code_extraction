# Make a list out of items in a sublist of a multidimensional list (python)
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M = [y for [x, y, z] in L]
