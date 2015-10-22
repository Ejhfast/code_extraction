# pandas python select all data after day of year
df2 = df[((df.index.month == 6) &amp; (df.index.day &gt; 20)) | (df.index.month &gt; 6)]
