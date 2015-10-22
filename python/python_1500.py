# Suppressing Cherrypy's output when running unit tests using Nose
cherrypy.config.update({ "environment": "embedded" })
