# How do I format a string using a dictionary in python-3.x?
geopoint = {'latitude':41.123,'longitude':71.091}
print('{latitude} {longitude}'.format(**geopoint))
