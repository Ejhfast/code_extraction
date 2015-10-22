# Convert Python UTC time stamp to local time in JavaScript
import datetime
utc_time = datetime.datetime.utcnow()
timestamp = (utc_time - datetime.datetime(1970, 1, 1)).total_seconds()
