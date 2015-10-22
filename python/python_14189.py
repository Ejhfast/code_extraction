# How to convert a date format like 'Wed Mar 13 10:10 EDT 2013' to "2013-03-13 10:10" in robot frame work or python
from dateutil.parser import parse as dateparser
dateparser("Wed Mar 13 10:10 EDT 2013").strftime("%Y-%m-%d %H:%M")
