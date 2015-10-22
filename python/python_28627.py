# For certain rows, copying values of a set of columns to another, of the same data frame
df[['col1', 'col2']] = df[df['col3'].isnull()][['col4', 'col5']]
