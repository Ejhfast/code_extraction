# Google app engine json response as REST
application = webapp.WSGIApplication([('/json', JsonPage)], debug=True)
