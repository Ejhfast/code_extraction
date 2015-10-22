# Removing the seconds from x-axis time labels in matplotlib
from matplotlib.dates import DateFormatter
formatter = DateFormatter('%H:%M')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
