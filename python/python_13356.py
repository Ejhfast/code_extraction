# Image as db.Blob() not showing from the DataStore
app = webapp2.WSGIApplication([('/admin', Admin), ('/', Main),('/img', Image)], debug=True)
