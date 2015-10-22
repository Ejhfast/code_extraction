# Plot volume planes in python mayavi with no voxel interpolation
from scipy.ndimage.interpolation import zoom
img3d2 = zoom(img3d, 4, order=0)
