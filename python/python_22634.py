# Pandas Plot: Index
ax = df2.plot(kind='bar', stacked=True)
ax.set_ylabel('Y Axis Label')
ax.set_xticklabels(df2.index, rotation='horizontal')
