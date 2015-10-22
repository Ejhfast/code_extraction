# Connect Twisted IRCClient through a http proxy
proxy = HTTPProxyConnector('myhttpproxy.server', 8080)
proxy.connectTCP('myirc.server', 6667, MyTwistedIRCClientFactory())
