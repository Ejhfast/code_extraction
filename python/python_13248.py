# Cherrypy: Getting app config settings when starting with cherryd
app = cherrypy.tree.mount(HelloWorld(), '/', 'tiny.cfg')
