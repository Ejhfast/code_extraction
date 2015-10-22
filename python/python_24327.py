# Efficient bit-testing conditional iteration over distinct array-elements
pixels, = np.where(bitflags &amp; FLAG)
for i, pixel in zip(pixels, array[pixels]):
    do_something(i, pixel)
