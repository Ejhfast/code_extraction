# Python socket.send() is not sent until socket is closed
send_bufr = "PRIVMSG %s :Hello %s\r\n" %(self.channel, sender)
print(send_bufr)
self.sock.send(bytearray(send_bufr, "utf-8"))
