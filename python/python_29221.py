# Updated: Matplotlib: Display numpy "sparse" array - Enlarge dots?
y, x = np.nonzero(ary)
plt.plot(x, y, '.', markersize=5)
