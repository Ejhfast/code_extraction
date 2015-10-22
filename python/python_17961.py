# Concatenation of numpy arrays of unknown dimension along arbitrary axis
newshapeA = A.shape + (1,) * (N + 1 - A.ndim)
