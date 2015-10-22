# how to remove the unecessay straight line in the plot?
mask = freq&gt;=0
pl.plot(freq[mask]*2*np.pi, np.sqrt(sp[mask].real**2+sp[mask].imag**2))
pl.plot(freq[~mask]*2*np.pi, np.sqrt(sp[~mask].real**2+sp[~mask].imag**2))
