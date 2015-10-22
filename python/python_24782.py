# Calculate min of rows ignoring NaN values
mins = list(np.min(np.ma.masked_array(a, np.isnan(a)), axis=1))
