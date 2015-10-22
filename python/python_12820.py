# How can I determine when the connection is broken?
import socket
self.request.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
