# Python - simplest and most coherent way to get timezone-aware current time in UTC?
import pytz
from datetime import datetime
now = datetime.utcnow().replace(tzinfo = pytz.utc)
