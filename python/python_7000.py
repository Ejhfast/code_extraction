# Using pandas, how do I subsample a large DataFrame by group in an efficient manner?
subsampled = df.ix[(choice(x) for x in grouped.groups.itervalues())]
