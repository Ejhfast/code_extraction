# python sys.stdin.read() unwanted split
source = sys.stdin.read()
for ip in source.split(","):
    print(geolite2.lookup(ip))
