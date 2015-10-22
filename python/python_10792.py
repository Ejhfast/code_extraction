# HTTP error: 403 while parsing a website
headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
req = urllib2.Request("http://dl.acm.org/dl.cfm", headers=headers)
urllib2.urlopen(req)
