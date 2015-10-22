# Why does Pandas DataFrame Resample change column Order
order = df.columns
return df.resample('W-Fri', how=ohlc_dict)[order]
