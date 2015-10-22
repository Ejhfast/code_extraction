# Segment Line Intersection algorithm in Numpy
r = np.array(intrsctd_pnts(A,B, axis_dx))
idx = np.where(np.sum(np.diff(r, axis=0)**2, -1) &lt; 1e-20)[0]+1
r2 = np.delete(r, idx, axis=0)
