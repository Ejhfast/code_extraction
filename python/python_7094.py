# How do I turn this date into a python datetime object?
from datetime import datetime
print datetime.strptime(timestring, '%Y-%m-%dT%H:%M:%SZ')
