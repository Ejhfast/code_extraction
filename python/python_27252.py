# Pandas cumulative/elementwise
a = df["Volume"].cumsum().clip_upper(20)
b = a.shift().fillna(0)
filled_a = a - b
