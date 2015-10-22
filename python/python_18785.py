# numpy array filtering twice and replace
m = b &lt; 6
b[m] = np.where(b[m]&lt; a,b[m],a)
