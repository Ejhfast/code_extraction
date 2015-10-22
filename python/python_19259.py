# Convert unicode to datetime proper strptime format
from datetime import datetime
date_posted = '2014-01-15T01:35:30.314Z'
datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%S.%fZ')
