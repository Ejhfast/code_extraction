# Need to use matplotlib scatter markers outside the chart, in labels for a bar graph
from matplotlib import rc
rc('text', usetex=True)
plt.xticks(ind+width/2., ("$\lozenge$", "$\square$", "$\plus$", "o", "$\bigtriangledown$") )
