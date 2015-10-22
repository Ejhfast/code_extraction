# getting error while using tcp.dport in dpkt
# Include the following condition in your for loop
if ip.p not in (dpkt.ip.IP_PROTO_TCP, dpkt.ip.IP_PROTO_UDP):
    continue
