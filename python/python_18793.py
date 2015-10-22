# Pandas datetime column to ordinal
df['date'].apply(lambda x: x.toordinal())
