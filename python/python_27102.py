# Unable to find a way to plot the data in matplotlib
df2 = churn_df.groupby(['states', 'CATEGORY'])    ['states'].count().unstack('CATEGORY').fillna(0)
df2[['good','bad']].plot(kind='bar', stacked=True, width=1)
