# Have CherryPy "submit" button launch external web page
@expose
def redirect(self, url):
    raise cherrypy.HTTPRedirect(url)
