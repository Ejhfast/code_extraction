# Getting 'pred_table' information for predicted values of a model in 'statsmodels'
import numpy as np
pred = np.array(mod_fit.predict(test) &gt; threshold, dtype=float)
table = np.histogram2d(test.Y, pred, bins=2)[0]
