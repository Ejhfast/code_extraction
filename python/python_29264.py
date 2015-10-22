# Getting microseconds past the hour
now = dt.now()
microseconds_past_the_hour = now.microsecond + 1000000*(now.minute*60 + now.second)
