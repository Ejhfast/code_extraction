# Python send JSON using HTTP POST
req = urllib2.Request(url, jsonString, {'Content-Type': 'application/json'})
