# Remove first and last IP from netaddr result
for ip in list(IPNetwork(ipc))[1:-1]:
