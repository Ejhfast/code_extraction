# Fast way to convert rgb to lab in python
from skimage import color
color.colorconv.lab_ref_white = np.array([0.96422, 1.0, 0.82521])
lab = color.rgb2lab(image)
