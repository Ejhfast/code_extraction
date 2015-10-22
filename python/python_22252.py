# Compare two columns in pandas DataFrame against the inverse
(df.src + df.dest).isin(df.dest + df.src)
