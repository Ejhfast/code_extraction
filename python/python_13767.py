# CherryPy: What would the html command line syntax be if you wanted to pass a dictionary as an argument?
@cherrypy.expose
def echo(self, *args, **kwargs):
    return kwargs['param_1']
