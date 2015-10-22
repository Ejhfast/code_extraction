# Converting timestamp with milliseconds to datetime in python
dt = datetime.fromtimestamp(1092847621L).replace(microsecond = 7100000L/1000)
