# Getting a datetime in this format and converting to 4 byte hex
import time
print hex(int(time.mktime(time.strptime('1999-12-31 15:00:00', '%Y-%m-%d %H:%M:%S'))) - time.timezone)
