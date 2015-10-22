# Trouble with aligning two y-axis ticks with matplotlib
lim1 = ax1.get_ylim()
lim2 = (lim1[0]*2, lim1[1] *2)
ax2.set_ylim(lim2)
