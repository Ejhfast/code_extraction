# how to send a post request using django
post_data = [('name','Gladys'),]     # a sequence of two element tuples
result = urllib2.urlopen('http://example.com', urllib.urlencode(post_data))
content = result.read()
