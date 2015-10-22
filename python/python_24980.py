# How should I decode HTTP headers from bytes to string?
request = conn.recv(2048)
headers, sep, body = request.partition(b'\r\n\r\n')
headers = headers.decode('latin1')
