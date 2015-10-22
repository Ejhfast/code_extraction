# Python one-liner for a confusion/contingency matrix needed
np.bincount(n * (Ytrue - 1) + (Ypred -1), minlength=n*n).reshape(n, n)
