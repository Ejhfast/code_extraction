# changing the xticks on a python plot
plt.imshow(grid_resid[:,:], aspect="auto")
plt.xticks(np.arange(grid_resid.shape[1]),xp)
plt.show()
