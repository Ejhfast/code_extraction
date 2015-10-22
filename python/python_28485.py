# How to turn this into a Python Datetime
from datetime import datetime
datetime.strptime("Tuesday July 7, 2015", "%A %B %d, %Y").strftime("%Y-%m-%d")
