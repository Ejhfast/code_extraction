# Split array at value in numpy
B= np.split(A, np.where(A[:, 0]== 0.)[0][1:])
