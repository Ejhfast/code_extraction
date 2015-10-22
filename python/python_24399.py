# How to transpose this dataframe?
pd.melt(df, id_vars=['Country Name', 'Series Code'], var_name='Year', value_name='your_values')
