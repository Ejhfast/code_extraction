# Python requests library - get SSL certificate information
f=my_opener.open(url)
f.fp._sock.fp._sock._sslobj # here's the ssl object holding the 'issuer' (CA) and 'server' (CN) attributes.
