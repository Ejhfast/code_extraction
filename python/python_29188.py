# matplotlib 3d contour_plot colour levels
cmap = matplotlib.pyplot.cm.Greys
bounds = numpy.linspace(numpy.amin(Z),numpy.amax(Z), n + 1)
normalisation = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
