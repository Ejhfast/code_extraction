# Convert IP address string to binary in Python
ip = '192.168.1.1'
print '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])
