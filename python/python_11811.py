# Slow Row-wise Comparison with For-loops in NumPy - How to improve?
for cfsXYZ in coordsCFS:
    match = numpy.nonzero(
        numpy.max(numpy.abs(coordRMED - cfsXYZ), axis=1) &lt; TOLERANCE)
