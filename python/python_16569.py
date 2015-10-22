# matplotlib contour plot with lognorm - colorbar levels
from matplotlib.ticker import LogFormatter
l_f = LogFormatter(10, labelOnlyBase=False)
cbar = plt.colorbar(CF, ticks=lvls, format=l_f)
