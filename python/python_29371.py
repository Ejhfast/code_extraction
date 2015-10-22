# Cannot get the average date using pandas
In [14]: pd.to_timedelta((s-s.min()).astype('m8[ms]').mean(),unit='ms')
Out[14]: Timedelta('249 days 12:00:00')
