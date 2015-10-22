# matplotlib pnpoly example results in error
from matplotlib.path import Path
path = Path(polygonVerts)
isInside = path.contains_point(point)
