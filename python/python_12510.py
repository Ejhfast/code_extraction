# How to get different point in ipython
badpoints = np.array(ginput(n=0))
index_badpoints = np.argmin(abs(np.subtract(badpoints[:,0],yeardays)),axis=1)
