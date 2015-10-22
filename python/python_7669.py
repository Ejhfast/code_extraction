# Can I create a static C array with Cython?
cdef int *shiftIndexes = [1,-1, 0, 2,-1, -1, 4, 0, -1, 8, 1, -1, 16, 1, 0, 32, 1, 1, 64, 0, 1, 128, -1, 1]
