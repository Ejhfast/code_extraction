# Extracting time from a line in Python
from datetime import datetime
val = '2013-01-09 06:13:51,464'.split(',')[0]  # Remove milliseconds
date_object = datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
