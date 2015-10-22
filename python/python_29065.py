# Subplots grid, legend outside, savefig does not work
lgd = axarr[k,l].legend(loc=(X,Y)) # X and Y such that outside of plot
plt.savefig("test.pdf", bbox_inches='tight', bbox_extra_artists=(lgd,))
