# Building a comet server from twisted.web, for a twisted.web site
from orbited.cometsession import Port
...
reactor.listenWith(Port, factory=someFactoryYouWrote, resource=someResourceYouWrote, childName='tcp')
