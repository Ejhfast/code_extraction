# Easiest way to combine date and time strings to single datetime object using Python
import datetime as dt
mytime = dt.datetime.strptime('0130','%H%M').time()
mydatetime = dt.datetime.combine(dt.date.today(), mytime)
