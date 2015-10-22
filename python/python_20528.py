# Pandas row manipulation
df1['foo'] = pd.merge(df1, df2, on='no', how='left').apply(lambda r: r['foo_y'] if r['foo_y'] == r['foo_y'] else r['foo_x'], axis=1)
