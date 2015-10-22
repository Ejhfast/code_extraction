# Python grequests with custom header
header = {'authorization' : '...'}
rs = (grequests.get(u, headers=header) for u in urls)
grequests.map(rs)
