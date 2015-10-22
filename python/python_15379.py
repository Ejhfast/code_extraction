# urllib2.urlopen addinfourl instance has not attribute '__getitem__'
url = 'http://data.mtgox.com/api/1/BTCUSD/ticker'
data = json.load(urllib2.urlopen(url))['return']
