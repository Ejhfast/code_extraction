# Pandas: convert a multiindex column headers into normal column header?
df = df.reset_index()
df.columns = list(df.columns)
