# Convert String In Python to insert into MySQL DB date column date
from dateutil.parser import parse
date = 'Thu, 14 Mar 2013 13:33:07 -0400'
parse(date).strftime("%Y-%m-%d %H:%M:%S")
