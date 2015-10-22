# How to separate Monday-Friday from Saturday and Sunday Pandas?
df['Monday-Friday'] = df['days'].isin(range(5)).astype(int)
df['Saturday'] = (df['days'] == 5).astype(int)
df['Sunday'] = (df['days'] == 6).astype(int)
