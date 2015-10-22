# Merge two files in Python PANDAS?
frames = [pd.read_csv('f1.csv'), pd.read_csv('f2.csv')]
result = concat(frames,ignore_index=True)
