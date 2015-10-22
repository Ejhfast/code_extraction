# Python telnetlib and console connection cisco node
s = socket.create_connection(('X.X.X.X', 2068))
data = s.recv(1024)
...
