# Python's `urllib2`: Why do I get error 403 when I `urlopen` a Wikipedia page?
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
con = urllib2.urlopen( req )
print con.read()
