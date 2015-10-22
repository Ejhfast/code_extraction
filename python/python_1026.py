# How to get a http page using mechanize cookies?
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.br._ua_handlers["_cookies"].cookiejar))
opener.open(imgurl)
