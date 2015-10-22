# Visualization of 3D-numpy-array frame by frame
def update(val):
    frame = numpy.around(sframe.val)
    l.set_data(data[frame,:,:])
