# python numpy/scipy find count or frequency of a relative variable in multi-dimensional array
import numpy as np
a = np.random.randint(0, 100, (100,128,256))
np.sum(a &gt; 10, axis=0)
