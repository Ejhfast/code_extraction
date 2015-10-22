# Filling higher-frequency windows when upsampling with pandas
s.reindex(DatetimeIndex(start=s.index[0].replace(day=1), end=s.index[-1], freq='D'))
