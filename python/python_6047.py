# ctypes pointer to numpy array with custom dtype
one = np.ascontiguousarray(a['one'])
one.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
