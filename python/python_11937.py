# pandas: count things
df = male_trips.groupby('start_station_id').size()
