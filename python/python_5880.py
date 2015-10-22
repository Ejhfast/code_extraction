# Speed up Matplotlib?
if(len(a) &gt; 1M):
   a = scipy.signal.decimate(a, int(len(a)/1M)+1)
pylab.plot(a)
