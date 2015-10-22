# Custom data types in numpy arrays
kerneldt = np.dtype([('myintname', np.int32), ('myfloats', np.float64, 9)])
arr = np.empty(dims, dtype=kerneldt)
