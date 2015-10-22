# Matplotlib axis tick format changes after zoom in ipython figure window
ax = pyplot.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
