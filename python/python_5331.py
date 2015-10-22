# In matplotlib.pyplot, how to plot two datasets using interleaved bar graphs?
pyplot.bar( numpy.arange(10) * 2, data1, color = 'red' )
pyplot.bar( numpy.arange(10) * 2 + 1, data2, color = 'red' )
