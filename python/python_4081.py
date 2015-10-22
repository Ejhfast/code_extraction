# Python: List of addressable IP addresses
l = list(netaddr.IPNetwork('192.168.0.0/27').iter_hosts())
