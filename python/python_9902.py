# How to convert the data and time according to given UTC offset using Pytz in python & django?
d = datetime.now(pytz.timezone('UTC'))   # get date in UTC format - you'll be getting it from the database
local = d.astimezone('Asia/Kolkata')
print local.strftime("%Y-%m-%d %H:%M:%S %z")
