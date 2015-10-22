# SimpleHTTPRequestHandler close connection before returning from do_POST method
self.finish()
self.connection.close()
