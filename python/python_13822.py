# Editing the date formatting of x-axis tick labels in matplotlib
import matplotlib.dates as mdates
myFmt = mdates.DateFormatter('%d')
ax.xaxis.set_major_formatter(myFmt)
