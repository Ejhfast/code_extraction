# Pandas- Create a new column filled with the number of observations in another column
df['num_totals'] = df.groupby('ID').transform('count')
