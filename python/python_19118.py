# improving Numpy dot performance by removing arrays copy
shape = (QT.shape[2],)*2
result = np.memmap('result.dat', dtype=QT.dtype, mode='w+', shape=shape)
np.dot(QT.T, QT, out=result)
