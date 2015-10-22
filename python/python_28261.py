# I can't import urllib2
from urllib.request import urlopen
html = urlopen("http://www.google.com/")
print(html)
