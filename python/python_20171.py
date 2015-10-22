# Python: Current UTC plus 30 minutes
from datetime import datetime
from datetime import timedelta
(datetime.utcnow() + timedelta(seconds=60*30)).strftime('%Y-%m-%d %H:%M:%S')
