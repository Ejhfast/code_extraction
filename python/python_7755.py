# Converting a cURL command to Python's urllib2
import urllib
tlds = urllib.urlopen("http://data.iana.org/TLD/tlds-alpha-by-domain.txt").readlines()
