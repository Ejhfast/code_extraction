# Distance calculation in hierarchical clustering "complete" linkage
import scipy.spatial.distance as ssd
distmatrix = ssd.squareform(distmatrix + distmatrix.T)
