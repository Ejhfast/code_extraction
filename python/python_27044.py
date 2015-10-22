# Find density of points from their scatter plot in python
from scipy import linalg as la
e = la.eigvals(my_matrix)
hist,xedges,yedges = np.histogram2d(e.real,e.imag,bins=40,normed=False)
