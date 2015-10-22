# numpy matrix to shared array for multiprocessing
Z_shared = Array('d', Z.size)
Z_shared[:] = Z.reshape((-1)) # copy entrywise
