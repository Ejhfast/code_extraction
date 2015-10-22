# HTTP SSL pipelining in Python
s = requests.session()
rs = [grequests.get(url, session=s) for url in urls]
grequests.map(rs)
