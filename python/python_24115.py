# Fastest way to convert ubyte [0, 255] array to float array [-0.5, +0.5] with NumPy
arr = numpy.memmap(f, '&gt;u1', 'r', shape=(size, rows, cols))
arr = arr / float(max_value)
arr -= 0.5
