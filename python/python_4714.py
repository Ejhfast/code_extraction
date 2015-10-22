# Python: get datetime for '3 years ago today'?
import datetime
datetime.datetime.now() - datetime.timedelta(days=3*365)
