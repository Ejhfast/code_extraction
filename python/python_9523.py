# Why this code gets this 'str' object has no attribute 'get_match_routes' error?
app = webapp2.WSGIApplication([(r'/', MainHandler),
                               (r'/welcome', WelcomeHandler)],
                               debug=True)
