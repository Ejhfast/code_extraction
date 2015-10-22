# pandas dataframe computation between columns
((df['x'] * df['y']).sum() - df['x'].sum() * df['y'].mean()) ** 2
