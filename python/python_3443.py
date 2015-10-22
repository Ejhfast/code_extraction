# Twisted UDP Server - daemonize?
import twisted.application
application = twisted.application.service.Application("Scotty's UDP server")
twisted.application.internet.UDPServer(PORT, BaseThreadedUDPServer()).setServiceParent(application)
