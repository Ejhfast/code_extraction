# How to change matplotlib axes so that that it does not display in scientific notation?
x_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
x_formatter.set_scientific(False)
ax.xaxis.set_major_formatter(x_formatter)
