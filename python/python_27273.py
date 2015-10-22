# Plotting Pandas Dataframe by Type
test.groupby(['id', 'type']).sum().unstack().plot(kind='bar')
