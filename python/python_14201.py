# Python, Socket error: [Errno 111] when trying to create 2 servers within the same file
interGrpSock.bind((host, port))
interGrpSock.listen(1)          /* Instead of s.listen(1) here */
