# Create ascending series of integers by group in Pandas
df['obs_num'] = 1
df['obs_num'] = df.groupby('Group')['obs_num'].cumsum()
