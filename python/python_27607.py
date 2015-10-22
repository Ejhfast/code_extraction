# Grouping a Pandas Dataframe by Date with Python and Plotting
df.groupby(df['Time'].dt.day).plot(x='Value1', y='Value2')
