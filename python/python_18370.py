# Passing numpy array to Cython
def dot(np.ndarray a, np.ndarray b):
    cdef np.ndarray d = np.dot(a, b)
    return d
