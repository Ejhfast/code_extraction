# What API, package or library is easiest to find the location of an IP address?
import urllib
response = urllib.urlopen('http://freegeoip.net/json/1.2.3.4').read()
print(response)
