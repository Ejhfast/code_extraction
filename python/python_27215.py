# Deleting Specific Rows from Pandas Dataframe
is_good = lambda group: group.isin(keep[group.name])
result = df[df.groupby('store_nbr')['item_nbr'].apply(is_good)]
