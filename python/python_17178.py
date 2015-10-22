# assigning to multi-dimensional array
tmp = C.swapaxes(1, 2)
tmp[:] = s
C = tmp.swapaxes(1, 2)
