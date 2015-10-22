# scipy.interpolate.griddata: cut z-value and get area inside it
if grid_z1.T[i][j] &gt; z0 or math.isnan(grid_z1.T[i][j]):
    grid_z1.T[i][j] = np.nan
