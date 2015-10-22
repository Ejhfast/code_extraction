# Socket connection won't close?
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
