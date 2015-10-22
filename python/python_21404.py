# Pandas: Sum of first N non-missing values per row
at_most=2
df.apply(lambda x: (x[np.isfinite(x)][:at_most]).sum(), axis=1)
