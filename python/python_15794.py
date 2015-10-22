# Strip down %Z to only return the timezone not daylight savings in python
time.strftime('%H:%M:%S %Z')[:13]
