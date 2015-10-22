# How to add seconds on a datetime value in Python?
from datetime import datetime, timedelta
x = datetime.now() + timedelta(seconds=3)
x += timedelta(seconds=3)
