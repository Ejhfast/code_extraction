# Slice pandas dataframe to get only oneday's data
df9 = df[(df['Time'] &gt; '2013-07-17 00:00') &amp; (df['Time'] &lt; '2013-07-17 23:59')]
