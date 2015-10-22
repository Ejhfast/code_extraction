# Use latin characters in appengine
Why are Google API queries through simplejson returning "responseData": null?
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&amp;q= ' + urllib.quote_plus(query)
