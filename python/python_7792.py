# webapp2 route fails
app = webapp2.WSGIApplication([('/', MainPage), ('/product/.*', MainPage)], debug=True)
