# How to combine Tornado authentication and AngularJS?
class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://yoursite.com")
