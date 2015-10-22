# How to manipulate columns of a data frame
df[df.names.index('a')] = df.rx2('a').ro / 10
