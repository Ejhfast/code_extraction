# Not getting the correct result back from inet_aton/struct.unpack
struct.unpack('&gt;L', socket.inet_aton('192.168.1.1'))[0]
