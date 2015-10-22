# Python package to work with GIS data?
from shapely.geometry import MultiPoint
points = MultiPoint([(0.0, 0.0), (1.0, 1.0)])
print points.centroid #True centroid, not necessarily an existing point
