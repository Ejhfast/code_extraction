# "TypeError: a float is required" occurred when using urllib2
req = urllib2.Request('https://api.twitter.com/oauth2/token', urllib.urlencode(data), headers)
resp = urllib2.urlopen(req)
