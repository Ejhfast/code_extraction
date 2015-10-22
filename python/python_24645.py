# Drop row in pandas dataframe if any value in the row equals zero
df[(df != 0).all(1)]
