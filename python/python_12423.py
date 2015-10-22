# Missing configuration keys for 'webapp2_extras.sessions': ['secret_key']
app = webapp2.WSGIApplication([('/path', MyHandler),
                              config=config,
                              debug=True)
