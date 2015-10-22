# How can I do DNS lookups in Python, including referring to /etc/hosts?
import socket
print socket.gethostbyname('localhost') # result from hosts file
print socket.gethostbyname('google.com') # your os sends out a dns query
