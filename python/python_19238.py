# Iterating within groups in Pandas
df.groupby(["Group", "stage"])["time"].apply(lambda x: x-x.iloc[0])
