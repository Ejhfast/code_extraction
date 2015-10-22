# Google App Engine SDK urlfetch workaround for openssl bug in Ubuntu 12.04
&lt; self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file)
---
&gt; self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)
