# Python join, why is it string.join(list) instead of list.join(string)?
import urllib2
print '\n############\n'.join(urllib2.urlopen('http://data.stackexchange.com/users/7095'))
