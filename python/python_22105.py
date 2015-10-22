# How to compare two timezones in python?
from datetime import datetime
today = datetime.today()
b.utcoffset(today) == c.utcoffset(today)
