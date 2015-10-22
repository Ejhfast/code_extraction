# How to send an integer over a socket to a Java application using python?
import struct
s.sendall(struct.pack('i', len(data)))
