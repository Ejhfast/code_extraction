# Python's mechanize proxy support
req = mechanize.Request("http://www.google.com")
req.set_proxy("localhost:8888","http")
mechanize.urlopen(req)
