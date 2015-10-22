# Pandas lookup, mapping one column in a dataframe to another in a different dataframe
df1 = df1.merge(df2[['weeknum', 'datetime']], on=['weeknum'])
