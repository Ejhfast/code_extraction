# Tunneling httplib Through a Proxy
import httplib
conn = httplib.HTTPConnection(proxyHost, proxyPort)
conn.request("POST", "http://www.google.com", params)
