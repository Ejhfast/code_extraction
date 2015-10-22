# matplotlib bar plot adjust bar direction
plt.bar(bins[:-1],abs(np.log10(1.*hist/N)),np.diff(bins))
