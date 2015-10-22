# Bad HTTP status code: 422
if e.status_code not in httplib.responses:
   logging.error("Bad HTTP status code: %d", e.status_code)
   self.send_error(500)
