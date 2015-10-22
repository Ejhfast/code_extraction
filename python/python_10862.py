# How to resample a python pandas TimeSeries containing dytpe Decimal values?
f = lambda x: Decimal(np.mean(x))
ts.resample('D', how = f)
