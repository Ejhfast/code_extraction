# HTTP Error 400 when trying to send json data with urllib2 to toggl api
req = urllib2.Request(url, data, {"Content-type": "application/json"})
