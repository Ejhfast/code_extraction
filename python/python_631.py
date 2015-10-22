# Mapping URL Pattern to a Single RequestHandler in a WSGIApplication
application=WSGIApplication([(r'.*',MyRequestHandler),])
