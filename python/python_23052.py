# dataframe boolean selection along columns instead of row
df.loc[:, df.iloc[0, :] &gt; 0.5]
