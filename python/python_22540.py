# How to pythonically get the max of a numpy argwhere function
A = np.argwhere(bins&lt;data)
print A[np.r_[A[1:,0] != A[:-1,0], True]]
