# How to get row delta value by pandas dataframe
df['delta'] = df.currentPrice.diff().shift(-1)
