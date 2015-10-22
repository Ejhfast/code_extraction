# Python Epoch Fail with 2-digit year
dt = datetime.datetime.strptime(dateVariable, "%b-%y")
if dt &gt; datetime.now():
    dt = dt - datetime.timedelta(years=100)
