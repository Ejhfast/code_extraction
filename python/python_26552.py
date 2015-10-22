# How to get status code for urllib2 in python 2.7
result = urllib2.urlopen(request)
contents = result.read()
print result.getcode()
