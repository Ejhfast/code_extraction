# how to get username on a page directed
self.redirect('/thanks?user=%s' % urllib.quote(self.request.get('username', 'new user')))
