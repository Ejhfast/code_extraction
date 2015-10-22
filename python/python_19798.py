# Value Error with color array when slicing values for scatter plot
timePlot = ax.scatter(x[::5], y[::5], s=50, c=timeList[::5], marker = marker.next(), edgecolors='none', norm=cNorm, cmap = plt.matplotlib.cm.jet)
