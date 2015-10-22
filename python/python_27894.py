# How to avoid program freezing when connecting to server
TIMEOUT = 5.0 # timeout in seconds
pythonwhois.net.socket.setdefaulttimeout(TIMEOUT)
pythonwhois.get_whois("example.com")
