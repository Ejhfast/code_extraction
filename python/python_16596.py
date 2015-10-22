# Python2 urllib/urllib2 wrong URL issue
data = urllib.urlencode({'abc': 'def', 'fgh': 'jkl'})
urllib2.urlopen(urllib2.Request('http://stackoverflow.com/index.php'))
