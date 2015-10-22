# Plot key count per unique value count in pandas
s = df.groupby("keys").ids.agg(lambda x:len(x.unique()))
pd.value_counts(s).plot(kind="bar")
