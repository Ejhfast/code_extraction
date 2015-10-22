# change X ticks in matplotlib plot
ax=plt.gca()
#ax.get_xticks() will get the current ticks
ax.set_xticklabels(map(str, ax.get_xticks()/5.0))
