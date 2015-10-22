# remove x ticks but keep grid lines
from matplotlib.ticker import NullFormatter
ax.xaxis.set_major_formatter(NullFormatter())
