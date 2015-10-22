# Create loglog plot of histogram data in xy style - python matplotlib
x = sorted( degree_frequencies.keys( ) )
y = [ degree_frequencies[ k ] for k in x ]
plt.loglog( x, y )
