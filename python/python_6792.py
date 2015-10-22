# Bind to mdns multicast address on mac os x
# For BSD based platforms.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.bind(('', MCAST_PORT))
