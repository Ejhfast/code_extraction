# pandas grouping based on hour to get intra day variability
hourly_series['hour'] = hourly_series.index
hourly_series['hour'] = hourly_series['hour'].apply(lambda x: x.hour)
hourly_series.groupby(['hour']).var() # Or any other stats function
