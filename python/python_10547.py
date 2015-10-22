# How use the mean method on a pandas TimeSeries with Decimal type values?
import numpy as np
ts.groupby([by('year'), by('month'), by('day')]).apply(lambda x: np.mean(x))
