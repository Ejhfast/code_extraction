# Linear regression of arrays containing NANs in Python/Numpy
mask = ~np.isnan(varx) &amp; ~np.isnan(vary)
slope, intercept, r_value, p_value, std_err = stats.linregress(varx[mask], vary[mask])
