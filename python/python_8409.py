# Convert UTC time from Datetimefield (models.py) to local time
local_time = zone.localize(timestamp)
