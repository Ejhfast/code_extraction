# ignore empty list when plotting histogram
pylab.hist([x for x in [data1,data2,data3] if len(x) &gt; 0], 10, normed=1, histtype='bar', stacked=True)
