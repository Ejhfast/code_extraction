# how to convert a datetime string back to datetime object?
from datetime import datetime
datetime.strptime("2010-11-13 10:33:54.227806", "%Y-%m-%d %H:%M:%S.%f")
