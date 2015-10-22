# urlencode not work
print urllib2.urlopen("%s?%s" % (url,urllib.urlencode({'nothing':12345}))).read()
