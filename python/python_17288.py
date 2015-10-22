# Numpy histogram on multi-dimensional array
hist, bin_edges = apply_along_axis(lambda x: histogram(x, bins=bins), 0, B)
