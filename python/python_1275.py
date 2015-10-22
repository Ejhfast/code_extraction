# paste.httpserver and slowdown with HTTP/1.1 Keep-alive; tested with httperf and ab
server.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
