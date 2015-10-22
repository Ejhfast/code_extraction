# Convert a column of timestamps into periods in pandas
df[1] = df[0].dt.to_period('M')
