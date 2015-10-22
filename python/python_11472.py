# Python server "Only one usage of each socket address is normally permitted"
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
