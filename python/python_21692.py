# Pandas cumsum using large amounts of memory
df['obs_num'] = df.groupby(["Index", "Date"]).cumcount() + 1
