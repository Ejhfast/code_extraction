# Normalize vector field by NumPy
norm = numpy.fmax(1.0, numpy.linalg.norm(var, axis=2))
res = var / norm[:, :, numpy.newaxis]
