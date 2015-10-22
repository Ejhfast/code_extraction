# How to handle both GET and POST requests in TornadoWeb framework?
class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.render('intro.html')
