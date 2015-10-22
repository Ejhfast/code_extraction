# Problems with datetime plot in matplotlib
import datetime
ax.plot_date([d.astype(datetime.datetime) for d in data['date']], data['count'])
