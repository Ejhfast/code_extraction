# Saving packets to a pcap file using Pcapy
dumper = pc.dump_open(filename)
...
dumper.dump(hrd, data)
