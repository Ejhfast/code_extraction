# Sort list of date strings
import datetime
d = ['09-2012', '04-2007', '11-2012', '05-2013', '12-2006', '05-2006', '08-2007']
sorted(d, key=lambda x: datetime.datetime.strptime(x, '%m-%Y'))
