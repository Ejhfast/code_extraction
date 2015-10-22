# Python read image to numpy array with multiprocessing
shared_arr = mp.Array(ctypes.c_double, N)
arr = tonumpyarray(shared_arr)
