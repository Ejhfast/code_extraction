# Find current time interval in python?
from datetime import datetime, timedelta
now = datetime.now()
now = now - timedelta(minutes = now.minute % 15, seconds = now.second, microseconds = now.microsecond )
