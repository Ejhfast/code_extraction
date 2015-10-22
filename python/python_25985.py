# Pandas: Map a function using multiple columns
df['d'] = df.apply(lambda x: some_func(a = x['a'], b = x['b'], c = x['c']))
