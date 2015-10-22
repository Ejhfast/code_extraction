# Tornado as normal server
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8000)
tornado.ioloop.IOLoop.instance().start()
