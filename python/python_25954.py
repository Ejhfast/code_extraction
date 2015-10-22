# How to make mpmath function return python float?
besseli_vec = numpy.frompyfunc(lambda *a: float(mpmath.besseli(*a)), 2, 1)
