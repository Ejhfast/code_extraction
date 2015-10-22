# How to change date format using matplolib in python
from matplotlib.dates import DateFormatter
formatter = DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
