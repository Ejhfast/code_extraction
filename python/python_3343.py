# My .yaml is not redirecting properly
application = webapp.WSGIApplication([('/user\.html', MainPage),
                                      ('/sign', UserWrite)],
                                     debug=True)
