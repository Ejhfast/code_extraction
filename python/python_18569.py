# Having two kinds of graphics in same ggplot
ggplot(aes(x=x), data=df_lng) + geom_line(aes(y=value, colour=variable), size=1.3) +
  geom_rect(aes(fill=factor(Back), xmin=x, xmax=x+1, ymin=0, ymax=max(value)*1.07), alpha=.1) +
  scale_fill_discrete(guide="none")
