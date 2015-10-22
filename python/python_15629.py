# Less frequent ticks on the x axis in Pyplot
locs = np.arange(grid_resid.shape[1],step=100) # locations
plt.xticks( locs, xp_int[locs], rotation="vertical" )
