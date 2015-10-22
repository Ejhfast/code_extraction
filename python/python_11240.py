# Rasterizing multiple elements in matplotlib
ax = fig.add_subplot(111, rasterized=True)
ax.plot(ts[0], ys.T, color='r', lw=0.5, alpha=0.5)
