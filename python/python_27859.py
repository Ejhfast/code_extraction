# ValueError: '10.0.0.0/24' does not appear to be an IPv4 or IPv6 network
import ipaddress
srcIp = ipaddress.ip_network(u'10.0.0.0/24')
print srcIp
