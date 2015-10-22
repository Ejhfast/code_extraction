# Get python ggplot bar axis right?
ggplot.ggplot(ggplot.aes(x='pips', weight='events'), frame) +
 ggplot.geom_bar(binwidth=1) +
 ggplot.scale_x_continuous(limits = (1,6), breaks = range(1,7))
