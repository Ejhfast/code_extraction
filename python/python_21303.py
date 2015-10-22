# pandas: Divide DataFrame last row by first row
df.T[df.index[0]] / df.T[df.index[-1]]
