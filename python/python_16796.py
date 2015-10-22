# sending "GET" request over proxy using httplib in python
import httplib
conn = httplib.HTTPConnection("10.1.1.19", 80)
conn.request("GET", "http://www.python.org/index.html", headers={...}))
