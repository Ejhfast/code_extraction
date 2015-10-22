# Create column from non null values in other column in Pandas
df.loc[df['ints'].notnull(),'ints'] = df['floats']
