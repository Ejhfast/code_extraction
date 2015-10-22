# Numpy : clip/cut 2d masked array
import numpy as np
si, se = np.where(~x.mask)
x = x[si.min():si.max() + 1, se.min():se.max() + 1]
