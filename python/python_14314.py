# Pycurl cannot connect to host
curl.setopt(pycurl.PROXY, "url")
curl.setopt(pycurl.PROXYPORT, 8000)
curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
