# Change Date in TimeSeries Dataframes Python
from pandas.tseries.offsets import DateOffset
df_volume.index = df_volume.index - DateOffset(months=7, days=10)
