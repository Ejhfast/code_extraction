# Heat Map Seaborn fmt='d' error
sns.heatmap(df3.pivot_table(index='Place', columns='Name',
values='00:00:00',aggfunc={'00:00:00':np.sum}), annot=True, fmt='.1f')
