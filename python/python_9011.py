# Python: How to read a data file with uneven number of columns
with open("hk_L1.ref") as f:
    data = numpy.array(f.read().split(), dtype=float).reshape(7000, 8)
