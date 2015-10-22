# Broadcast pandas.Series.div column-wise to a DataFrame
In [24]: my_df.apply(lambda x: my_series.div(x)).shape
 Out[24]: (1504, 4)
