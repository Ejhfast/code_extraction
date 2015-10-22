# Pandas selection keeping the same shape as original DataFrame
import numpy as np
df.B[(df.B &lt; 10) | (df.B &gt; 70)] = np.nan
df.C[df.C != 200] = np.nan
