# Unexpected result when upsampling hourly values using the pandas resample function
&gt;&gt;&gt; ts.resample('D', how='mean', closed="left", loffset=datetime.timedelta(days=-1))
2012-01-01    0.200299
