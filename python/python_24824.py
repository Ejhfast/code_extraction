# Python: Pandas plot histogram with centered x-values
bar = pd.DataFrame(maxdf['maxnet'].value_counts())
bar = bar.sort()
bar.plot(kind='bar')
