# How to include all points into error-less triangulation mesh with scipy.spatial.Delaunay?
points -= points.mean(axis=0)
tri = Delaunay(points)
