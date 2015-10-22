# Pylons Custom Middleware return 404
if error:
    start_response("404 Not Found", [('Content-type', 'text/plain')])
    return ['Page not found']
