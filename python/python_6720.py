# Change Cherrypy Port and restart web server
import cherrypy
cherrypy.config.update({'server.socket_port': 8099})
cherrypy.engine.restart()
