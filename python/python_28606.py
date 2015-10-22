# Using colorbar with secondary y axis
cbaxes = fig.add_axes([1, 0.15, 0.03, 0.7])
plt.colorbar(img, label=r"Height (cm)",format='%1.1f', ax=ax1, cax=cbaxes)
