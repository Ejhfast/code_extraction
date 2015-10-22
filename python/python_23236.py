# django timezone: How to compare time difference in days between 2 days across DST
In [79]: import datetime as DT
In [80]: (DT.datetime.combine(event1, DT.time(0)) - DT.datetime.combine(event2, DT.time(0))).days
Out[80]: 1
