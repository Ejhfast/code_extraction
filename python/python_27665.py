# TCP Receive in Python, reading the data out
def readlines(self):
    data = self.sock.recv(1024).decode()
    print(data)
