# How to fetch json argument in handler (json is in body of post request with no key to json)
data = tornado.escape.json_decode(self.request.body)
