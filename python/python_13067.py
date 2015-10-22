# pandas efficient way to get first filtered row for each DatetimeIndex entry
result = df[df.pct_change &lt; -0.015].reindex(filtered_dates, method='bfill')
