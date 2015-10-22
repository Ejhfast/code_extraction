# Colorbar for two contour plots
fig = plt.figure()
ax2 = fig.add_axes([0.9, 0.1, 0.05, 0.9])
fig.colorbar(z1, cax=ax2) #specifies to put the colorbar in ax2
