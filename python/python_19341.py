# Get rows that have the same value across its columns in pandas
df[df.apply(lambda x: min(x) == max(x), 1)]
