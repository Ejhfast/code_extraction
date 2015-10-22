# HTTPS GET request & read JSON reply
import json
import urllib2
data = json.loads(urllib2.urlopen(url).read())
