# GAE multiple WSGI files for multiple URL handlers
app = webapp2.WSGIApplication([('/blog/?', BlogPage), ('/blog/newpost', NewPost)], debug=True)
