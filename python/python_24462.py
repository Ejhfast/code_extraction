# Tick marks disappear on secondary x-axis in Matplotlib
TicksNum = len(par1.xaxis.get_major_ticks())
par2.xaxis.set_major_locator(MaxNLocator(nbins = TicksNum) )
par2.xaxis.set_ticklabels([0, r'$1.5\times 10^{8}', r'$1.5\times10^{9}', r'$7.3\times10^{9}', r'$2.4\times10^{10}', r'$6.1\times10^{10}', r'$1.2\times10^{11}', r'$2.0\times10^{11}', r'$2.9\times10^{11}', r'$3.6\times10^{11}', 0])
