# WSGI - Set content type to JSON
self.response.headers['Content-Type'] = "application/json"
self.response.out.write(json.dumps(response))
