# Reverse dns lookup with scapy in python
sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1,qd=DNSQR(qname="211.196.59.69.in-addr.arpa", qtype='PTR')))
