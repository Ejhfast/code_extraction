# Why am I getting an is_monotonic assertion error using pandas Series.asfreq
nlsn['Adj Close'][::-1].asfreq('M', method='ffill')
