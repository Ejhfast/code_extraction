# Unable to open a URL link with using urllib2 in chrome
url = 'http://www.klse.info/companies/listed-companies/alphabet/A'
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
page = urllib2.urlopen(req).read()
