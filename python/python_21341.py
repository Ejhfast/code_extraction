# How to convert a CIDR prefix to a dotted-quad netmask in Python?
def cidr(prefix):
    return socket.inet_ntoa(struct.pack("&gt;I", (0xffffffff &lt;&lt; (32 - prefix)) &amp; 0xffffffff))
