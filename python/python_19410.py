# Pandas: merging Series values
df.loc[df['shape'].isin(['round', 'square']), 'shape'] = 'other'
