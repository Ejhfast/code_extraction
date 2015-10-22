# How to remove trailer of the packet in python using scapy
packet_without_trailer=IP(str(packet[IP])[0:packet[IP].len])
