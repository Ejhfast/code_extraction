# Silencing cherrypy
logger = cherrypy.log.access_log
logger.removeHandler(logger.handlers[0])
