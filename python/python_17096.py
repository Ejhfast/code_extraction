# Python - error 98 Adress already in use, how to make it faster? So that on kill and quick restart it does not fail?
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
