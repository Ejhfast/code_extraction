# Find the number of turns in path (set of coordinates)
arr = np.array(a)
((np.abs(arr[2:] - arr[:-2])&gt;0).sum(axis=1)==2).sum()
