# Using timeit on a cython function
print timeit.timeit(stmt='offset_back(10000,1000,1000)',setup='from offset_back import offset_back',number=1000)
