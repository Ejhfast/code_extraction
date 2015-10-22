# Matplotlib label y axis
ax.set_ylim(0.1, 1)
import matplotlib.ticker as tick
ax.yaxis.set_major_locator(tick.MultipleLocator(0.1))
