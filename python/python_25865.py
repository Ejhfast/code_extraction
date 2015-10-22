# Pandas TimerGrouper: Index with beginning
df.groupby([pd.TimeGrouper("MS", label='left'), 'status']).sum()
