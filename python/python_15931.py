# how to get favicon.ico work on tornado
handlers = [
    (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""}),
 ]
