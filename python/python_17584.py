# Resampling Pandas Series with integer index (add missing index)
max_range = max(s.index) + 1
s = s.reindex(index=range(1, max_range), fill_value=0)
