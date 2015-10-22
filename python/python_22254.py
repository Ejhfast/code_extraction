# How would I plot a graph of the number of non-NaNs per column in pandas?
ser = df.count()
ser.sort(ascending=False)
ser.plot(ser.plot(kind='barh')
