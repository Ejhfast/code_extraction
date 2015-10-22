# Matplotlib: plotting data labels on data connected to parasite axis
for (x,y) in zip(times, difference):
    if y:
         par.annotate("{0}%".format(y), xy=(x, y+10))
