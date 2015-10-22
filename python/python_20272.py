# Trying to run GAE python - not sure if imports and app.yaml is configured correctly
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
