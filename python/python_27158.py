# Scapy and TCP stack: avoid the TCP stack of my system to send an RST
iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 192.168.2.68 -j DROP
