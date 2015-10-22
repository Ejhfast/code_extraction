# how to combine two columns with an if/else in python pandas?
df['year'] = df['year'].where(source_years!=0,df['year'])
