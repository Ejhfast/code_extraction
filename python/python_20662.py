# MPI.Op and performing operation
buffers = [[1,1],[2,2]]
result = reduce(MPI.SUM, buffers)
