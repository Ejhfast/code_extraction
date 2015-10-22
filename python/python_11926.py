# Python: how to make an histogram with equally *sized* bins
from scipy import stats
bin_edges = stats.mstats.mquantiles(data, [0, 2./6, 4./6, 1])
&gt;&gt; array([1. , 1.24666667, 2.05333333, 2.12])
