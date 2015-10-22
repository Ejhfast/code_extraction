# How can I convert a Python datetime object to UTC?
from datetime import datetime, timedelta
datetime.utcnow() + timedelta(minutes=5)
