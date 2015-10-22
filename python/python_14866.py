# What is the best way to make the matrix operations more faster in python
eij = rating_train[i, j] - np.dot(P[i, :], Q[:, j])
P[i, :] += alpha * (2 * eij * Q[:, j] - beta * P[i, :])
Q[:, j] += alpha * (2 * eij * P[i, :] - beta * Q[:, j])
