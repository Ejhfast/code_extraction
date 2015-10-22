# Pandas groupby and file writing problems
for group_name, group_df in df.head(1000).groupby('iid'):
    item_grouper(group_df)
