# Split pandas dataframe based on groupby
gb = df.groupby('ZZ')
[gb.get_group(x) for x in gb.groups]
