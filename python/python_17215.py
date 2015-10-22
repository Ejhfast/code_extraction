# extract indices from multi dimensional array using condition, max
idx = np.argmax(sliceB &gt;= 35, axis=1) # index of first occurrence of condition
sliceA[np.arange(sliceA.shape[0]), idx]
