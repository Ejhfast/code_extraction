# Does Google appengine cache external requests?
result = urlfetch.fetch(url, headers = {'Cache-Control' : 'max-age=240'})
