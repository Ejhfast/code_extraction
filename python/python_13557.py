# Specifying packet length with scapy
payload = 'ZZZZZZZZZZZZZZZZZZZZZ'
pkt = Ether() / IP() / TCP() / payload
