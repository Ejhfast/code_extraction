# Pandas: Add column if does not exists
if 'Met' not in df:
    df['Met'] = df['freqC'] * df['coverage']
