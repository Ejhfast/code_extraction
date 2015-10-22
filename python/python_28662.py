# Join two elements as a tuple, which can be a tuple themselved or not
a = (1, 2)
b = 3
joined = (a if isinstance(a, tuple) else (a,)) + (b if isinstance(b, tuple) else (b,))
