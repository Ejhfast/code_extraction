# Numpy vectorization of 2D array differences
dA = A[1:, :-1] - A[:-1, :-1]
dB = B[:-1, 1:] - B[:-1, :-1]
C = dA * dB
