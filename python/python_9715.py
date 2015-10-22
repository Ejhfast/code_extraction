# How to make a redirect and keep the query string?
newurl = '/my/new/route?' + urllib.urlencode(self.request.params)
self.redirect(newurl)
